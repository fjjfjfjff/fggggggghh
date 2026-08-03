from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputMediaAnimation
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from bot.config import settings, GIF_FILE_ID
from bot.database.queries import get_or_create_user, get_user_by_referral
from bot.keyboards.main_menu import main_menu_kb, language_kb
from bot.locales.texts import get_text

router = Router()


async def send_main_menu(target, lang: str, edit: bool = False):
    text = get_text(lang, "welcome")
    kb = main_menu_kb(settings.WEBAPP_URL)
    if edit and isinstance(target, CallbackQuery):
        try:
            await target.message.edit_media(
                media=InputMediaAnimation(media=GIF_FILE_ID, caption=text, parse_mode="HTML"),
                reply_markup=kb,
            )
        except Exception:
            await target.message.answer_animation(
                animation=GIF_FILE_ID,
                caption=text,
                parse_mode="HTML",
                reply_markup=kb,
            )
    else:
        msg = target.message if isinstance(target, CallbackQuery) else target
        await msg.answer_animation(
            animation=GIF_FILE_ID,
            caption=text,
            parse_mode="HTML",
            reply_markup=kb,
        )


@router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject, session: AsyncSession, state: FSMContext):
    await state.clear()
    args = command.args or ""
    user = await get_or_create_user(session, message.from_user.id, message.from_user.username)

    if args.startswith("ref_"):
        referral_code = args[4:]
        referrer = await get_user_by_referral(session, referral_code)
        if referrer and referrer.telegram_id != message.from_user.id and not user.referred_by:
            user.referred_by = referrer.telegram_id
            await session.commit()

    if args.startswith("deal_") or (len(args) == 10 and not args.startswith("ref_")):
        deal_id = args.replace("deal_", "")
        from bot.handlers.deals import show_deal_card
        await show_deal_card(message, session, deal_id, user)
        return

    await send_main_menu(message, user.language)


@router.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: CallbackQuery, session: AsyncSession, state: FSMContext):
    await state.clear()
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    await send_main_menu(callback, user.language, edit=True)
    await callback.answer()


@router.callback_query(F.data == "change_language")
async def change_language(callback: CallbackQuery, session: AsyncSession):
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    text = get_text(user.language, "choose_language")
    try:
        await callback.message.edit_caption(caption=text, parse_mode="HTML", reply_markup=language_kb())
    except Exception:
        await callback.message.answer(text, parse_mode="HTML", reply_markup=language_kb())
    await callback.answer()


@router.callback_query(F.data.startswith("set_lang:"))
async def set_language(callback: CallbackQuery, session: AsyncSession):
    lang = callback.data.split(":")[1]
    from bot.database.queries import update_user_language
    await update_user_language(session, callback.from_user.id, lang)
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    user.language = lang
    await send_main_menu(callback, lang, edit=True)
    await callback.answer()


@router.callback_query(F.data == "appeals")
async def show_appeals(callback: CallbackQuery, session: AsyncSession):
    from bot.keyboards.main_menu import appeals_kb
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    text = get_text(user.language, "appeals")
    try:
        await callback.message.edit_caption(caption=text, parse_mode="HTML", reply_markup=appeals_kb())
    except Exception:
        await callback.message.answer(text, parse_mode="HTML", reply_markup=appeals_kb())
    await callback.answer()


@router.callback_query(F.data == "appeals_stub")
async def appeals_stub(callback: CallbackQuery, session: AsyncSession):
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    await callback.answer(get_text(user.language, "appeals_stub"), show_alert=True)


@router.callback_query(F.data == "referrals")
async def show_referrals(callback: CallbackQuery, session: AsyncSession):
    from bot.keyboards.main_menu import back_to_menu_red_kb
    user = await get_or_create_user(session, callback.from_user.id, callback.from_user.username)
    from bot.database.queries import get_user
    from sqlalchemy import select, func
    from bot.database.models import User
    result = await session.execute(
        select(func.count()).where(User.referred_by == user.telegram_id)
    )
    invited_count = result.scalar() or 0
    text = get_text(
        user.language, "referrals",
        bot_username=settings.BOT_USERNAME,
        referral_code=user.referral_code,
        invited_count=invited_count,
        bonus=round(user.referral_bonus, 2),
    )
    try:
        await callback.message.edit_caption(caption=text, parse_mode="HTML", reply_markup=back_to_menu_red_kb())
    except Exception:
        await callback.message.answer(text, parse_mode="HTML", reply_markup=back_to_menu_red_kb())
    await callback.answer()
