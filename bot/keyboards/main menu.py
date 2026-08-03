from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.config import EMOJI, CHANNEL_URL, SUPPORT_URL, LANGUAGES, CARD_REGIONS


def btn(text: str, emoji_key: str = None, **kwargs) -> InlineKeyboardButton:
    """Создаёт кнопку с кастомным эмодзи и зелёным стилем."""
    params = {
        "text": text,
        "style": "success",  # зелёный цвет кнопки
    }
    if emoji_key and EMOJI.get(emoji_key):
        params["icon_custom_emoji_id"] = EMOJI[emoji_key]
    params.update(kwargs)
    return InlineKeyboardButton(**params)


def main_menu_kb(webapp_url: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        btn("Создать сделку", "cart", callback_data="create_deal")
    )
    builder.row(
        btn("Мой баланс", "money", callback_data="balance"),
        btn("Реквизиты", "clipboard", callback_data="requisites"),
    )
    builder.row(
        btn("Канал ↗", "channel", url=CHANNEL_URL),
        btn("Обращения", "appeals", callback_data="appeals"),
    )
    builder.row(
        btn("Рефералы", "referral", callback_data="referrals"),
        btn("Поддержка ↗", "support", url=SUPPORT_URL),
    )
    builder.row(
        btn("Мини-приложение ↗", "appeals", web_app={"url": webapp_url})
    )
    builder.row(
        btn("Изменить язык", "language", callback_data="change_language")
    )
    return builder.as_markup()


def language_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for code, label in LANGUAGES.items():
        builder.row(InlineKeyboardButton(
            text=label,
            callback_data=f"set_lang:{code}",
            style="success",
        ))
    return builder.as_markup()


def choose_role_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn("Я продавец", "money", callback_data="role:seller"))
    builder.row(btn("Я покупатель", "cart", callback_data="role:buyer"))
    builder.row(btn("Вернуться в меню", "back", callback_data="main_menu"))
    return builder.as_markup()


def choose_type_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn("NFT-Подарок / Подарок", "gift", callback_data="type:nft_gift"))
    builder.row(btn("Канал / Чат", "channel", callback_data="type:channel"))
    builder.row(btn("Звезды", "stars", callback_data="type:stars"))
    builder.row(btn("NFT-юзернеймы / Тег", "tag", callback_data="type:username"))
    builder.row(btn("Другое", "other", callback_data="type:other"))
    builder.row(btn("Отмена", "cancel", callback_data="main_menu"))
    return builder.as_markup()


def choose_payment_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn("На TON-Кошелек", "sparkles", callback_data="payment:ton"))
    builder.row(btn("Перевод На карту / СБП", "sparkles", callback_data="payment:card"))
    builder.row(btn("Звезды", "stars", callback_data="payment:stars"))
    builder.row(btn("Вернуться в меню", "cancel", callback_data="main_menu"))
    return builder.as_markup()


def cancel_to_menu_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn("Вернуться в меню", "cancel", callback_data="main_menu"))
    return builder.as_markup()


def deal_created_kb() -> InlineKeyboardMarkup:
    return cancel_to_menu_kb()


def deal_buyer_kb(deal_id: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn("Подтвердить оплату", "check", callback_data=f"confirm_payment:{deal_id}"))
    builder.row(btn("Выйти со сделки", "cancel", callback_data=f"exit_deal:{deal_id}"))
    return builder.as_markup()


def seller_notify_kb(deal_id: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn("Подтвердить передачу товара", "check", callback_data=f"confirm_transfer:{deal_id}"))
    builder.row(btn("Отменить сделку", "cancel", callback_data=f"cancel_deal:{deal_id}"))
    return builder.as_markup()


def appeals_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        btn("Предложить", callback_data="appeals_stub"),
        btn("Пожаловаться", callback_data="appeals_stub"),
    )
    builder.row(btn("Назад", "back", callback_data="main_menu"))
    return builder.as_markup()


def requisites_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn("Добавить/Изменить TON-Кошелек", "add", callback_data="add_ton"))
    builder.row(btn("Добавить карту / номер телефона", "add", callback_data="add_card"))
    builder.row(btn("Вернуться в меню", "back_red", callback_data="main_menu"))
    return builder.as_markup()


def card_region_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for region in CARD_REGIONS:
        builder.button(text=region, callback_data=f"region:{region}", style="success")
    builder.adjust(2)
    builder.row(btn("Вернуться в меню", "back_red", callback_data="main_menu"))
    return builder.as_markup()


def back_to_menu_red_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn("Вернуться в меню", "back_red", callback_data="main_menu"))
    return builder.as_markup()


def balance_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn("Вывести средства", "cash", callback_data="withdraw"))
    builder.row(btn("История операций", "scroll", callback_data="operations"))
    builder.row(btn("Вернуться в меню", "back", callback_data="main_menu"))
    return builder.as_markup()
