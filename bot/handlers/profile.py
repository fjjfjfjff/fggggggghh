from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaAnimation
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from bot.config import GIF_FILE_ID
from bot.database.queries import (
    get_or_create_user, get_or_create_requisite,
    update_ton_wallet, update_card, get_user_operations,
)
from bot.keyboards.main_menu import (
    balance_kb, requisites_kb, card_region_kb, back_to_menu_red_kb,
)
from bot.locales.texts import get_text
from bot.states.deal_states import RequisiteStates

router = Router()


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


@router.callback_query(F.data == "balance")
async def show_balance(callback: CallbackQuery, session: AsyncSession):
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    req = await get_or_create_requisite(session, user.telegram_id)

    ton_status = get_text(user.language, "added") if req.ton_wallet else get_text(user.language, "not_added")
    card_status = get_text(user.language, "added") if req.card_number else get_text(user.language, "not_added")

    text = get_text(
        user.language, "balance",
        username=user.username or str(user.telegram_id),
        balance_rub=round(user.balance_rub, 2),
        balance_ton=round(user.balance_ton, 4),
        balance_stars=round(user.balance_stars, 2),
        ton_status=ton_status,
        card_status=card_status,
        deals_count=user.successful_deals,
    )

    await edit_or_send(callback, text, balance_kb(lang=user.language))
    await callback.answer()


@router.callback_query(F.data == "withdraw")
async def show_withdraw(callback: CallbackQuery, session: AsyncSession):
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    text = get_text(user.language, "withdraw_info")
    await edit_or_send(callback, text, back_to_menu_red_kb(lang=user.language))
    await callback.answer()


@router.callback_query(F.data == "operations")
async def show_operations(callback: CallbackQuery, session: AsyncSession):
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    ops = await get_user_operations(session, user.telegram_id)

    if not ops:
        text = get_text(user.language, "operations_empty")
    else:
        header = get_text(user.language, "operations_header")
        lines = []
        for op in ops:
            date_str = op.created_at.strftime("%d.%m.%Y")
            lines.append(f"• {date_str} — {op.description or op.type}: {op.amount} {op.currency.upper()}")
        text = header + "\n".join(lines)

    await edit_or_send(callback, text, back_to_menu_red_kb(lang=user.language))
    await callback.answer()


@router.callback_query(F.data == "requisites")
async def show_requisites(callback: CallbackQuery, session: AsyncSession):
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    req = await get_or_create_requisite(session, user.telegram_id)

    ton_status = get_text(user.language, "added") if req.ton_wallet else get_text(user.language, "not_added")
    card_status = get_text(user.language, "added") if req.card_number else get_text(user.language, "not_added")

    text = get_text(
        user.language, "requisites",
        ton_status=ton_status,
        card_status=card_status,
    )

    await edit_or_send(callback, text, requisites_kb(lang=user.language))
    await callback.answer()


@router.callback_query(F.data == "add_ton")
async def add_ton_wallet(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    await state.set_state(RequisiteStates.entering_ton_wallet)
    text = get_text(user.language, "enter_ton_wallet")
    await edit_or_send(callback, text, back_to_menu_red_kb(lang=user.language))
    await callback.answer()


@router.message(RequisiteStates.entering_ton_wallet)
async def save_ton_wallet(message: Message, session: AsyncSession, state: FSMContext):
    user = await get_or_create_user(session, message.from_user.id, message.from_user.username)
    wallet = (message.text or "").strip()
    if len(wallet) < 10:
        await message.answer("Некорректный адрес кошелька. Попробуйте снова.", reply_markup=back_to_menu_red_kb(lang=user.language))
        return
    await update_ton_wallet(session, user.telegram_id, wallet)
    await state.clear()
    text = get_text(user.language, "ton_wallet_saved")
    await message.answer_animation(
        animation=GIF_FILE_ID,
        caption=text,
        parse_mode="HTML",
        reply_markup=back_to_menu_red_kb(lang=user.language),
    )


@router.callback_query(F.data == "add_card")
async def add_card_start(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    await state.set_state(RequisiteStates.choosing_card_region)
    text = get_text(user.language, "choose_card_region")
    await edit_or_send(callback, text, card_region_kb(lang=user.language), gif=False)
    await callback.answer()


@router.callback_query(F.data.startswith("region:"), RequisiteStates.choosing_card_region)
async def choose_region(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    region = callback.data.split(":", 1)[1]
    await state.update_data(card_region=region)
    await state.set_state(RequisiteStates.entering_card_number)
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    text = get_text(user.language, "enter_card_number")
    await edit_or_send(callback, text, back_to_menu_red_kb(lang=user.language), gif=False)
    await callback.answer()


@router.message(RequisiteStates.entering_card_number)
async def save_card(message: Message, session: AsyncSession, state: FSMContext):
    user = await get_or_create_user(session, message.from_user.id, message.from_user.username)
    card = (message.text or "").strip().replace(" ", "")
    if len(card) < 10:
        await message.answer("Некорректные реквизиты. Попробуйте снова.", reply_markup=back_to_menu_red_kb(lang=user.language))
        return
    data = await state.get_data()
    region = data.get("card_region", "")
    await update_card(session, user.telegram_id, card, region)
    await state.clear()
    text = get_text(user.language, "card_saved")
    await message.answer_animation(
        animation=GIF_FILE_ID,
        caption=text,
        parse_mode="HTML",
        reply_markup=back_to_menu_red_kb(lang=user.language),
    )
