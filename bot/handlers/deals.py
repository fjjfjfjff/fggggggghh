import re
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaAnimation
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from bot.config import settings, GIF_FILE_ID
from bot.database.queries import (
    get_or_create_user, get_deal, create_deal,
    set_deal_buyer, update_deal_status, complete_deal, get_user,
)
from bot.database.models import DealStatus
from bot.keyboards.main_menu import (
    choose_role_kb, choose_type_kb, choose_payment_kb,
    cancel_to_menu_kb, deal_created_kb, deal_buyer_kb,
    seller_notify_kb, back_to_menu_red_kb,
)
from bot.locales.texts import get_text, get_deal_type_label, get_payment_label
from bot.states.deal_states import DealCreation

router = Router()

CURRENCY_LABELS = {
    "ton": "TON",
    "card": "RUB",
    "stars": "Stars",
}

DESCRIPTION_KEYS = {
    "nft_gift": "enter_description_nft_gift",
    "channel": "enter_description_channel",
    "stars": "enter_description_stars",
    "username": "enter_description_username",
    "other": "enter_description_other",
}


def validate_amount(text: str) -> float | None:
    text = text.strip().replace(",", ".")
    try:
        val = float(text)
        if val <= 0:
            return None
        return round(val, 4)
    except ValueError:
        return None


def validate_description(text: str, deal_type: str) -> bool:
    if deal_type in ("nft_gift", "channel", "username"):
        links = text.strip().splitlines()
        pattern = re.compile(r"^(https?://|t\.me/)\S+$")
        return all(pattern.match(link.strip()) for link in links if link.strip())
    return len(text.strip()) >= 3


async def edit_or_send(callback: CallbackQuery, text: str, kb, gif: bool = True):
    if gif:
        try:
            await callback.message.edit_media(
                media=InputMediaAnimation(media=GIF_FILE_ID, caption=text, parse_mode="HTML"),
                reply_markup=kb,
            )
        except Exception:
            await callback.message.answer_animation(
                animation=GIF_FILE_ID, caption=text, parse_mode="HTML", reply_markup=kb
            )
    else:
        try:
            await callback.message.edit_caption(caption=text, parse_mode="HTML", reply_markup=kb)
        except Exception:
            await callback.message.answer(text, parse_mode="HTML", reply_markup=kb)


@router.callback_query(F.data == "create_deal")
async def create_deal_start(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    await state.set_state(DealCreation.choosing_role)
    text = get_text(user.language, "choose_role")
    await edit_or_send(callback, text, choose_role_kb(lang=user.language))
    await callback.answer()


@router.callback_query(F.data.startswith("role:"), DealCreation.choosing_role)
async def choose_role(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    role = callback.data.split(":")[1]
    await state.update_data(role=role)
    await state.set_state(DealCreation.choosing_type)
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    text = get_text(user.language, "choose_type")
    await edit_or_send(callback, text, choose_type_kb(lang=user.language))
    await callback.answer()


@router.callback_query(F.data.startswith("type:"), DealCreation.choosing_type)
async def choose_type(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    deal_type = callback.data.split(":")[1]
    await state.update_data(deal_type=deal_type)
    await state.set_state(DealCreation.choosing_payment)
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    deal_type_label = get_deal_type_label(user.language, deal_type)
    text = get_text(user.language, "choose_payment", deal_type=deal_type_label)
    await edit_or_send(callback, text, choose_payment_kb(lang=user.language))
    await callback.answer()


@router.callback_query(F.data.startswith("payment:"), DealCreation.choosing_payment)
async def choose_payment(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    payment = callback.data.split(":")[1]
    await state.update_data(payment=payment)
    await state.set_state(DealCreation.entering_amount)
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    currency = CURRENCY_LABELS.get(payment, payment.upper())
    text = get_text(user.language, "enter_amount", currency=currency)
    await edit_or_send(callback, text, cancel_to_menu_kb(lang=user.language))
    await callback.answer()


@router.message(DealCreation.entering_amount)
async def enter_amount(message: Message, session: AsyncSession, state: FSMContext):
    user = await get_or_create_user(session, message.from_user.id, message.from_user.username)
    amount = validate_amount(message.text or "")
    if amount is None:
        await message.answer(
            get_text(user.language, "err_invalid_amount"),
            reply_markup=cancel_to_menu_kb(lang=user.language)
        )
        return
    await state.update_data(amount=amount)
    await state.set_state(DealCreation.entering_description)
    data = await state.get_data()
    deal_type = data.get("deal_type", "other")
    text_key = DESCRIPTION_KEYS.get(deal_type, "enter_description_other")
    text = get_text(user.language, text_key)
    await message.answer_animation(
        animation=GIF_FILE_ID,
        caption=text,
        parse_mode="HTML",
        reply_markup=cancel_to_menu_kb(lang=user.language),
    )


@router.message(DealCreation.entering_description)
async def enter_description(message: Message, session: AsyncSession, state: FSMContext):
    user = await get_or_create_user(session, message.from_user.id, message.from_user.username)
    data = await state.get_data()
    deal_type = data.get("deal_type", "other")
    role = data.get("role", "seller")
    description = message.text or ""

    if not validate_description(description, deal_type):
        await message.answer(
            get_text(user.language, "err_invalid_format"),
            reply_markup=cancel_to_menu_kb(lang=user.language),
        )
        return

    payment = data.get("payment", "ton")
    amount = data.get("amount", 0.0)

    # Если покупатель создаёт сделку — seller_id остаётся None до прихода продавца
    # Но по логике бота сделку ВСЕГДА создаёт продавец.
    # Если роль = buyer — показываем ошибку, сделку создаёт только продавец.
    if role == "buyer":
        await message.answer(
            get_text(user.language, "err_buyer_cant_create"),
            reply_markup=cancel_to_menu_kb(lang=user.language),
        )
        return

    deal = await create_deal(
        session=session,
        seller_id=user.telegram_id,
        deal_type=deal_type,
        payment_method=payment,
        amount=amount,
        description=description,
    )

    await state.clear()

    currency_label = CURRENCY_LABELS.get(payment, payment.upper())
    deal_type_label = get_deal_type_label(user.language, deal_type)

    text = get_text(
        user.language, "deal_created",
        amount=amount,
        currency_label=currency_label,
        deal_type=deal_type_label,
        description=description,
        bot_username=settings.BOT_USERNAME,
        deal_id=deal.deal_id,
    )

    await message.answer_animation(
        animation=GIF_FILE_ID,
        caption=text,
        parse_mode="HTML",
        reply_markup=deal_created_kb(lang=user.language),
    )


async def show_deal_card(message: Message, session: AsyncSession, deal_id: str, user):
    deal = await get_deal(session, deal_id)
    if not deal:
        await message.answer(
            get_text(user.language, "err_deal_not_found"),
            reply_markup=back_to_menu_red_kb(lang=user.language)
        )
        return

    if deal.seller_id == user.telegram_id:
        await message.answer(
            get_text(user.language, "err_you_are_seller"),
            reply_markup=back_to_menu_red_kb(lang=user.language),
        )
        return

    if deal.status not in (DealStatus.PENDING, DealStatus.ACTIVE):
        await message.answer(
            get_text(user.language, "err_deal_closed"),
            reply_markup=back_to_menu_red_kb(lang=user.language)
        )
        return

    updated_deal = await set_deal_buyer(session, deal_id, user.telegram_id)
    if not updated_deal:
        await message.answer(
            get_text(user.language, "err_join_failed"),
            reply_markup=back_to_menu_red_kb(lang=user.language)
        )
        return

    seller = await get_user(session, deal.seller_id)
    seller_username = seller.username if seller and seller.username else str(deal.seller_id)

    currency_label = CURRENCY_LABELS.get(deal.payment_method, deal.payment_method)
    deal_type_label = get_deal_type_label(user.language, deal.deal_type if isinstance(deal.deal_type, str) else deal.deal_type.value)
    payment_label = get_payment_label(user.language, deal.payment_method if isinstance(deal.payment_method, str) else deal.payment_method.value)

    text = get_text(
        user.language, "deal_card_buyer",
        deal_id=deal.deal_id,
        seller_username=seller_username,
        description=deal.description,
        deal_type=deal_type_label,
        payment_method=payment_label,
        amount=deal.amount,
        currency_label=currency_label,
    )

    await message.answer_animation(
        animation=GIF_FILE_ID,
        caption=text,
        parse_mode="HTML",
        reply_markup=deal_buyer_kb(deal.deal_id, lang=user.language),
    )

    join_text = get_text(
        user.language, "user_joined_deal",
        username=user.username or str(user.telegram_id),
        deal_id=deal.deal_id,
        deals_count=user.successful_deals,
    )
    try:
        seller_lang = seller.language if seller else "ru"
        seller_join_text = get_text(
            seller_lang, "user_joined_deal",
            username=user.username or str(user.telegram_id),
            deal_id=deal.deal_id,
            deals_count=user.successful_deals,
        )
        await message.bot.send_animation(
            chat_id=deal.seller_id,
            animation=GIF_FILE_ID,
            caption=seller_join_text,
            parse_mode="HTML",
        )
    except Exception:
        pass


@router.callback_query(F.data.startswith("confirm_payment:"))
async def confirm_payment(callback: CallbackQuery, session: AsyncSession):
    deal_id = callback.data.split(":")[1]
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    deal = await get_deal(session, deal_id)

    if not deal or deal.buyer_id != user.telegram_id:
        await callback.answer(get_text(user.language, "err_not_buyer"), show_alert=True)
        return

    if deal.status != DealStatus.ACTIVE:
        await callback.answer(get_text(user.language, "err_cant_confirm"), show_alert=True)
        return

    await update_deal_status(session, deal_id, DealStatus.PAID)

    text_buyer = get_text(user.language, "payment_confirmed_buyer")
    await edit_or_send(callback, text_buyer, back_to_menu_red_kb(lang=user.language))

    seller = await get_user(session, deal.seller_id)
    seller_lang = seller.language if seller else "ru"
    currency_label = CURRENCY_LABELS.get(
        deal.payment_method if isinstance(deal.payment_method, str) else deal.payment_method.value,
        "TON"
    )

    notify_text = get_text(
        seller_lang, "payment_notify_seller",
        buyer_username=user.username or str(user.telegram_id),
        deal_id=deal.deal_id,
        description=deal.description,
        amount=deal.amount,
        currency_label=currency_label,
        commission=deal.commission,
        amount_after=deal.amount_after_commission,
    )

    try:
        await callback.bot.send_animation(
            chat_id=deal.seller_id,
            animation=GIF_FILE_ID,
            caption=notify_text,
            parse_mode="HTML",
            reply_markup=seller_notify_kb(deal.deal_id, lang=seller_lang),
        )
    except Exception:
        pass

    await callback.answer()


@router.callback_query(F.data.startswith("exit_deal:"))
async def exit_deal(callback: CallbackQuery, session: AsyncSession):
    from bot.handlers.start import send_main_menu
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    await send_main_menu(callback, user.language, edit=True)
    await callback.answer()


@router.callback_query(F.data.startswith("confirm_transfer:"))
async def confirm_transfer(callback: CallbackQuery, session: AsyncSession):
    """Продавец подтверждает передачу товара — отправляем покупателю запрос подтверждения."""
    deal_id = callback.data.split(":")[1]
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    deal = await get_deal(session, deal_id)

    if not deal or deal.seller_id != user.telegram_id:
        await callback.answer(get_text(user.language, "err_not_seller"), show_alert=True)
        return

    if deal.status != DealStatus.PAID:
        await callback.answer(get_text(user.language, "err_cant_complete"), show_alert=True)
        return

    # Меняем статус на TRANSFERRED — ждём подтверждения от покупателя
    await update_deal_status(session, deal_id, DealStatus.TRANSFERRED)

    # Продавцу показываем — ждём покупателя
    text_seller = get_text(user.language, "transfer_waiting_buyer")
    await edit_or_send(callback, text_seller, back_to_menu_red_kb(lang=user.language))

    # Покупателю отправляем уведомление с кнопкой подтверждения
    buyer = await get_user(session, deal.buyer_id)
    if buyer:
        buyer_lang = buyer.language if buyer else "ru"
        currency_label = CURRENCY_LABELS.get(
            deal.payment_method if isinstance(deal.payment_method, str) else deal.payment_method.value,
            "TON"
        )
        notify_text = get_text(
            buyer_lang, "transfer_notify_buyer",
            seller_username=user.username or str(user.telegram_id),
            deal_id=deal.deal_id,
            amount=deal.amount,
            currency_label=currency_label,
        )
        from bot.keyboards.main_menu import confirm_receive_kb
        try:
            await callback.bot.send_animation(
                chat_id=deal.buyer_id,
                animation=GIF_FILE_ID,
                caption=notify_text,
                parse_mode="HTML",
                reply_markup=confirm_receive_kb(deal.deal_id, lang=buyer_lang),
            )
        except Exception:
            pass

    await callback.answer()


@router.callback_query(F.data.startswith("confirm_receive:"))
async def confirm_receive(callback: CallbackQuery, session: AsyncSession):
    """Покупатель подтверждает получение товара — сделка завершается."""
    deal_id = callback.data.split(":")[1]
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    deal = await get_deal(session, deal_id)

    if not deal or deal.buyer_id != user.telegram_id:
        await callback.answer(get_text(user.language, "err_not_buyer"), show_alert=True)
        return

    if deal.status != DealStatus.TRANSFERRED:
        await callback.answer(get_text(user.language, "err_cant_complete"), show_alert=True)
        return

    await complete_deal(session, deal_id)

    currency_label = CURRENCY_LABELS.get(
        deal.payment_method if isinstance(deal.payment_method, str) else deal.payment_method.value,
        "TON"
    )

    # Покупателю — сделка завершена
    text_buyer = get_text(user.language, "deal_completed_buyer", deal_id=deal.deal_id)
    await edit_or_send(callback, text_buyer, back_to_menu_red_kb(lang=user.language))

    # Продавцу — уведомление о завершении + зачисление
    seller = await get_user(session, deal.seller_id)
    if seller:
        seller_lang = seller.language if seller else "ru"
        text_seller = get_text(
            seller_lang, "deal_completed_seller",
            amount_after=deal.amount_after_commission,
            currency_label=currency_label,
            deal_id=deal.deal_id,
        )
        try:
            await callback.bot.send_animation(
                chat_id=deal.seller_id,
                animation=GIF_FILE_ID,
                caption=text_seller,
                parse_mode="HTML",
                reply_markup=back_to_menu_red_kb(lang=seller_lang),
            )
        except Exception:
            pass

    await callback.answer()


@router.callback_query(F.data.startswith("cancel_deal:"))
async def cancel_deal(callback: CallbackQuery, session: AsyncSession):
    deal_id = callback.data.split(":")[1]
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    deal = await get_deal(session, deal_id)

    if not deal or deal.seller_id != user.telegram_id:
        await callback.answer(get_text(user.language, "err_not_seller"), show_alert=True)
        return

    await update_deal_status(session, deal_id, DealStatus.CANCELLED)
    from bot.handlers.start import send_main_menu
    await send_main_menu(callback, user.language, edit=True)
    await callback.answer()
