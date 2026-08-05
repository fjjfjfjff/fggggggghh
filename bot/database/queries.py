import uuid
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from bot.database.models import User, Requisite, Deal, Operation, DealStatus


async def get_or_create_user(session: AsyncSession, telegram_id: int, username: str | None = None) -> User:
    result = await session.execute(select(User).where(User.telegram_id == telegram_id))
    user = result.scalar_one_or_none()
    if not user:
        referral_code = uuid.uuid4().hex[:8].upper()
        user = User(
            telegram_id=telegram_id,
            username=username,
            referral_code=referral_code,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
    else:
        if username and user.username != username:
            user.username = username
            await session.commit()
    return user


async def get_user(session: AsyncSession, telegram_id: int) -> User | None:
    result = await session.execute(select(User).where(User.telegram_id == telegram_id))
    return result.scalar_one_or_none()


async def get_user_by_referral(session: AsyncSession, referral_code: str) -> User | None:
    result = await session.execute(select(User).where(User.referral_code == referral_code))
    return result.scalar_one_or_none()


async def update_user_language(session: AsyncSession, telegram_id: int, language: str) -> None:
    await session.execute(
        update(User).where(User.telegram_id == telegram_id).values(language=language)
    )
    await session.commit()


async def get_or_create_requisite(session: AsyncSession, user_id: int) -> Requisite:
    result = await session.execute(select(Requisite).where(Requisite.user_id == user_id))
    req = result.scalar_one_or_none()
    if not req:
        req = Requisite(user_id=user_id)
        session.add(req)
        await session.commit()
        await session.refresh(req)
    return req


async def update_ton_wallet(session: AsyncSession, user_id: int, wallet: str) -> None:
    result = await session.execute(select(Requisite).where(Requisite.user_id == user_id))
    req = result.scalar_one_or_none()
    if req:
        req.ton_wallet = wallet
    else:
        req = Requisite(user_id=user_id, ton_wallet=wallet)
        session.add(req)
    await session.commit()


async def update_card(session: AsyncSession, user_id: int, card: str, region: str) -> None:
    result = await session.execute(select(Requisite).where(Requisite.user_id == user_id))
    req = result.scalar_one_or_none()
    if req:
        req.card_number = card
        req.card_region = region
    else:
        req = Requisite(user_id=user_id, card_number=card, card_region=region)
        session.add(req)
    await session.commit()


async def create_deal(
    session: AsyncSession,
    seller_id: int | None,
    deal_type: str,
    payment_method: str,
    amount: float,
    description: str,
    buyer_id: int | None = None,
) -> Deal:
    from bot.config import COMMISSION
    commission = round(amount * COMMISSION, 4)
    after = round(amount - commission, 4)
    deal = Deal(
        seller_id=seller_id,
        buyer_id=buyer_id,
        deal_type=deal_type,
        payment_method=payment_method,
        amount=amount,
        commission=commission,
        amount_after_commission=after,
        description=description,
    )
    session.add(deal)
    await session.commit()
    await session.refresh(deal)
    return deal


async def get_deal(session: AsyncSession, deal_id: str) -> Deal | None:
    result = await session.execute(select(Deal).where(Deal.deal_id == deal_id))
    return result.scalar_one_or_none()


async def set_deal_buyer(session: AsyncSession, deal_id: str, buyer_id: int) -> Deal | None:
    deal = await get_deal(session, deal_id)
    if deal and deal.buyer_id is None:
        deal.buyer_id = buyer_id
        deal.status = DealStatus.ACTIVE
        await session.commit()
        await session.refresh(deal)
    return deal


async def set_deal_seller(session: AsyncSession, deal_id: str, seller_id: int) -> Deal | None:
    deal = await get_deal(session, deal_id)
    if deal and deal.seller_id is None:
        deal.seller_id = seller_id
        deal.status = DealStatus.ACTIVE
        await session.commit()
        await session.refresh(deal)
    return deal


async def update_deal_status(session: AsyncSession, deal_id: str, status: DealStatus) -> None:
    await session.execute(
        update(Deal).where(Deal.deal_id == deal_id).values(status=status)
    )
    await session.commit()


async def complete_deal(session: AsyncSession, deal_id: str) -> Deal | None:
    from datetime import datetime
    deal = await get_deal(session, deal_id)
    if deal:
        deal.status = DealStatus.COMPLETED
        deal.completed_at = datetime.utcnow()
        seller = await get_user(session, deal.seller_id)
        if seller:
            if deal.payment_method == "ton":
                seller.balance_ton = round(seller.balance_ton + deal.amount_after_commission, 4)
            elif deal.payment_method == "card":
                seller.balance_rub = round(seller.balance_rub + deal.amount_after_commission, 4)
            elif deal.payment_method == "stars":
                seller.balance_stars = round(seller.balance_stars + deal.amount_after_commission, 4)
            seller.successful_deals += 1
        buyer = await get_user(session, deal.buyer_id)
        if buyer:
            buyer.successful_deals += 1
        op = Operation(
            user_id=deal.seller_id,
            type="deal_income",
            amount=deal.amount_after_commission,
            currency=deal.payment_method,
            deal_id=deal.deal_id,
            description=f"Сделка #{deal.deal_id} завершена",
        )
        session.add(op)
        await session.commit()
        await session.refresh(deal)
    return deal


async def get_user_operations(session: AsyncSession, user_id: int) -> list[Operation]:
    result = await session.execute(
        select(Operation)
        .where(Operation.user_id == user_id)
        .order_by(Operation.created_at.desc())
        .limit(20)
    )
    return list(result.scalars().all())


async def add_operation(
    session: AsyncSession,
    user_id: int,
    op_type: str,
    amount: float,
    currency: str,
    deal_id: str | None = None,
    description: str | None = None,
) -> Operation:
    op = Operation(
        user_id=user_id,
        type=op_type,
        amount=amount,
        currency=currency,
        deal_id=deal_id,
        description=description,
    )
    session.add(op)
    await session.commit()
    await session.refresh(op)
    return op
