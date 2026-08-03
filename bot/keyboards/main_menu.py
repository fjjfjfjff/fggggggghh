from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.config import EMOJI, CHANNEL_URL, SUPPORT_URL, LANGUAGES, CARD_REGIONS
from bot.locales.texts import ce


def main_menu_kb(webapp_url: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("cart")} Создать сделку',
            callback_data="create_deal",
        )
    )
    builder.row(
        InlineKeyboardButton(text=f'{ce("money")} Мой баланс', callback_data="balance"),
        InlineKeyboardButton(text=f'{ce("clipboard")} Реквизиты', callback_data="requisites"),
    )
    builder.row(
        InlineKeyboardButton(text=f'{ce("channel")} Канал ↗', url=CHANNEL_URL),
        InlineKeyboardButton(text=f'{ce("appeals")} Обращения', callback_data="appeals"),
    )
    builder.row(
        InlineKeyboardButton(text=f'{ce("referral")} Рефералы', callback_data="referrals"),
        InlineKeyboardButton(text=f'{ce("support")} Поддержка ↗', url=SUPPORT_URL),
    )
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("appeals")} Мини-приложение ↗',
            web_app={"url": webapp_url},
        )
    )
    builder.row(
        InlineKeyboardButton(text=f'{ce("language")} Изменить язык', callback_data="change_language"),
    )
    return builder.as_markup()


def language_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for code, label in LANGUAGES.items():
        builder.row(InlineKeyboardButton(text=label, callback_data=f"set_lang:{code}"))
    return builder.as_markup()


def choose_role_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("money")} Я продавец',
            callback_data="role:seller",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("cart")} Я покупатель',
            callback_data="role:buyer",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("back")} Вернуться в меню',
            callback_data="main_menu",
        )
    )
    return builder.as_markup()


def choose_type_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text=f'{ce("gift")} NFT-Подарок / Подарок', callback_data="type:nft_gift")
    )
    builder.row(
        InlineKeyboardButton(text=f'{ce("channel")} Канал / Чат', callback_data="type:channel")
    )
    builder.row(
        InlineKeyboardButton(text=f'{ce("stars")} Звезды', callback_data="type:stars")
    )
    builder.row(
        InlineKeyboardButton(text=f'{ce("tag")} NFT-юзернеймы / Тег', callback_data="type:username")
    )
    builder.row(
        InlineKeyboardButton(text=f'{ce("other")} Другое', callback_data="type:other")
    )
    builder.row(
        InlineKeyboardButton(text=f'{ce("cancel")} Отмена', callback_data="main_menu")
    )
    return builder.as_markup()


def choose_payment_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("sparkles")} На TON-Кошелек',
            callback_data="payment:ton",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("sparkles")} Перевод На карту / СБП',
            callback_data="payment:card",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("stars")} Звезды',
            callback_data="payment:stars",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("cancel")} Вернуться в меню',
            callback_data="main_menu",
        )
    )
    return builder.as_markup()


def cancel_to_menu_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("cancel")} Вернуться в меню',
            callback_data="main_menu",
        )
    )
    return builder.as_markup()


def deal_created_kb() -> InlineKeyboardMarkup:
    return cancel_to_menu_kb()


def deal_buyer_kb(deal_id: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Подтвердить оплату", callback_data=f"confirm_payment:{deal_id}")
    )
    builder.row(
        InlineKeyboardButton(text="Выйти со сделки", callback_data=f"exit_deal:{deal_id}")
    )
    return builder.as_markup()


def seller_notify_kb(deal_id: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Подтвердить передачу товара", callback_data=f"confirm_transfer:{deal_id}")
    )
    builder.row(
        InlineKeyboardButton(text="Отменить сделку", callback_data=f"cancel_deal:{deal_id}")
    )
    return builder.as_markup()


def appeals_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Предложить", callback_data="appeals_stub"),
        InlineKeyboardButton(text="Пожаловаться", callback_data="appeals_stub"),
    )
    builder.row(
        InlineKeyboardButton(text="Назад", callback_data="main_menu"),
    )
    return builder.as_markup()


def requisites_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("add")} Добавить/Изменить TON-Кошелек',
            callback_data="add_ton",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("add")} Добавить карту / номер телефона',
            callback_data="add_card",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("back_red")} Вернуться в меню',
            callback_data="main_menu",
        )
    )
    return builder.as_markup()


def card_region_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for region in CARD_REGIONS:
        builder.button(text=region, callback_data=f"region:{region}")
    builder.adjust(2)
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("back_red")} Вернуться в меню',
            callback_data="main_menu",
        )
    )
    return builder.as_markup()


def back_to_menu_red_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=f'{ce("back_red")} Вернуться в меню',
            callback_data="main_menu",
        )
    )
    return builder.as_markup()


def balance_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Вывести средства", callback_data="withdraw")
    )
    builder.row(
        InlineKeyboardButton(text="История операций", callback_data="operations")
    )
    builder.row(
        InlineKeyboardButton(text="Вернуться в меню", callback_data="main_menu")
    )
    return builder.as_markup()
