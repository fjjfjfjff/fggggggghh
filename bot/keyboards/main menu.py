from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.config import EMOJI, CHANNEL_URL, SUPPORT_URL, LANGUAGES, CARD_REGIONS
from bot.locales.texts import ce, get_text


def btn(text: str, emoji_key: str = None, **kwargs) -> InlineKeyboardButton:
    params = {"text": text, "style": "success"}
    if emoji_key and EMOJI.get(emoji_key):
        params["icon_custom_emoji_id"] = EMOJI[emoji_key]
    params.update(kwargs)
    return InlineKeyboardButton(**params)


def t(lang: str, key: str) -> str:
    return get_text(lang, key)


def main_menu_kb(webapp_url: str, lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_create_deal"), "cart", callback_data="create_deal"))
    builder.row(
        btn(t(lang, "btn_balance"), "money", callback_data="balance"),
        btn(t(lang, "btn_requisites"), "clipboard", callback_data="requisites"),
    )
    builder.row(
        btn(t(lang, "btn_channel"), "channel", url=CHANNEL_URL),
        btn(t(lang, "btn_appeals"), "appeals", callback_data="appeals"),
    )
    builder.row(
        btn(t(lang, "btn_referrals"), "referral", callback_data="referrals"),
        btn(t(lang, "btn_support"), "support", url=SUPPORT_URL),
    )
    builder.row(btn(t(lang, "btn_mini_app"), "appeals", web_app={"url": webapp_url}))
    builder.row(btn(t(lang, "btn_change_lang"), "language", callback_data="change_language"))
    return builder.as_markup()


def language_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for code, label in LANGUAGES.items():
        builder.row(InlineKeyboardButton(text=label, callback_data=f"set_lang:{code}", style="success"))
    return builder.as_markup()


def choose_role_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_seller"), "money", callback_data="role:seller"))
    builder.row(btn(t(lang, "btn_buyer"), "cart", callback_data="role:buyer"))
    builder.row(btn(t(lang, "btn_back_menu"), "back", callback_data="main_menu"))
    return builder.as_markup()


def choose_type_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_nft_gift"), "gift", callback_data="type:nft_gift"))
    builder.row(btn(t(lang, "btn_channel_type"), "channel", callback_data="type:channel"))
    builder.row(btn(t(lang, "btn_stars"), "stars", callback_data="type:stars"))
    builder.row(btn(t(lang, "btn_username"), "tag", callback_data="type:username"))
    builder.row(btn(t(lang, "btn_other"), "other", callback_data="type:other"))
    builder.row(btn(t(lang, "btn_cancel"), "cancel", callback_data="main_menu"))
    return builder.as_markup()


def choose_payment_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_ton_payment"), "sparkles", callback_data="payment:ton"))
    builder.row(btn(t(lang, "btn_card_payment"), "sparkles", callback_data="payment:card"))
    builder.row(btn(t(lang, "btn_stars_payment"), "stars", callback_data="payment:stars"))
    builder.row(btn(t(lang, "btn_cancel"), "cancel", callback_data="main_menu"))
    return builder.as_markup()


def cancel_to_menu_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_back_menu"), "cancel", callback_data="main_menu"))
    return builder.as_markup()


def deal_created_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    return cancel_to_menu_kb(lang)


def deal_buyer_kb(deal_id: str, lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_confirm_payment"), "check", callback_data=f"confirm_payment:{deal_id}"))
    builder.row(btn(t(lang, "btn_exit_deal"), "cancel", callback_data=f"exit_deal:{deal_id}"))
    return builder.as_markup()


def seller_notify_kb(deal_id: str, lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_confirm_transfer"), "check", callback_data=f"confirm_transfer:{deal_id}"))
    builder.row(btn(t(lang, "btn_cancel_deal"), "cancel", callback_data=f"cancel_deal:{deal_id}"))
    return builder.as_markup()


def appeals_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        btn(t(lang, "btn_suggest"), callback_data="appeals_stub"),
        btn(t(lang, "btn_complain"), callback_data="appeals_stub"),
    )
    builder.row(btn(t(lang, "btn_back"), "back", callback_data="main_menu"))
    return builder.as_markup()


def requisites_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_add_ton"), "add", callback_data="add_ton"))
    builder.row(btn(t(lang, "btn_add_card"), "add", callback_data="add_card"))
    builder.row(btn(t(lang, "btn_back_menu"), "back_red", callback_data="main_menu"))
    return builder.as_markup()


def card_region_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for region in CARD_REGIONS:
        builder.button(text=region, callback_data=f"region:{region}", style="success")
    builder.adjust(2)
    builder.row(btn(t(lang, "btn_back_menu"), "back_red", callback_data="main_menu"))
    return builder.as_markup()


def back_to_menu_red_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_back_menu"), "back_red", callback_data="main_menu"))
    return builder.as_markup()


def balance_kb(lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_withdraw"), "cash", callback_data="withdraw"))
    builder.row(btn(t(lang, "btn_operations"), "scroll", callback_data="operations"))
    builder.row(btn(t(lang, "btn_back_menu"), "back", callback_data="main_menu"))
    return builder.as_markup()

def confirm_receive_kb(deal_id: str, lang: str = "ru") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(btn(t(lang, "btn_confirm_receive"), "check", callback_data=f"confirm_receive:{deal_id}"))
    builder.row(btn(t(lang, "btn_back_menu"), "back_red", callback_data="main_menu"))
    return builder.as_markup()

