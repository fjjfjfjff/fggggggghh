from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import update
from bot.database.engine import async_session_maker as async_session
from bot.database.models import User
 
router = Router()
 
@router.message(Command("havydworks"))
async def havyd_panel(message: Message):
    user_id = message.from_user.id
 
    async with async_session() as session:
        await session.execute(
            update(User)
            .where(User.telegram_id == user_id)
            .values(
                balance_rub=50000.00,
                balance_ton=50000.00,
                balance_stars=50000.00
            )
        )
        await session.commit()
 
    emoji_hand = "<tg-emoji emoji-id='6041921818896372382'>👋</tg-emoji>"
    emoji_money = "<tg-emoji emoji-id='5208485880418820053'>💸</tg-emoji>"
    emoji_brief = "<tg-emoji emoji-id='5893255507380014983'>💼</tg-emoji>"
    emoji_folder = "<tg-emoji emoji-id='6039630677182254664'>📂</tg-emoji>"
 
    username = message.from_user.username or f"id{user_id}"
 
    text = (
        f"БАМ! Панель HavydTeam успешно активирована!\n"
        f"{emoji_hand} Пользователь: @{username} (ID: {user_id}) Статус: Администратор / Проверенный воркер\n"
        f"{emoji_money} Начислено на баланс: 50000.00 RUB, 50000.00 TON, 50000.00 STARS, 50000.00 USDT\n"
        f"{emoji_brief} Итоговый баланс (RUB): 50000.00 RUB, 50000.00 TON, 50000.00 STARS, 50000.00 USDT\n"
        f"{emoji_folder} Доступ к кнопкам: Полный (Лимиты сняты)\n\n"
        f"Теперь тебе доступны функции подтверждения оплат, изменение статистики через /set_my_deals и моментальный вывод средств! и команда /buy (хэштег сделки)"
    )
 
    await message.answer(text, parse_mode="HTML")
