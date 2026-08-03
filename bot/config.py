from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List


class Settings(BaseSettings):
    BOT_TOKEN: str
    DATABASE_URL: str
    REDIS_URL: str
    ADMIN_IDS: List[int]
    BOT_USERNAME: str
    WEBAPP_URL: str

    @field_validator("ADMIN_IDS", mode="before")
    @classmethod
    def parse_admin_ids(cls, v):
        if isinstance(v, str):
            return [int(x.strip()) for x in v.split(",")]
        return v

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()

EMOJI = {
    "wave":         "6041921818896372382",
    "briefcase":    "5893255507380014983",
    "sparkles":     "5893321843149902412",
    "card":         "5902056028513505203",
    "shield":       "6030445631921721471",
    "cart":         "5278613311858959074",
    "money":        "5276037216244624892",
    "clipboard":    "5278227821364275264",
    "channel":      "5278778882848220741",
    "appeals":      "5278589204207528856",
    "referral":     "5298668674532538341",
    "support":      "5276381204470329471",
    "language":     "5278753302023004775",
    "choose":       "5276262671962892944",
    "back":         "5278578973595427038",
    "cancel":       "5774077015388852135",
    "gift":         "5429610910148748577",
    "stars":        "5848259999763011021",
    "tag":          "5278589204207528856",
    "other":        "5278227821364275264",
    "check":        "6030445631921721471",
    "scroll":       "5363967308601501461",
    "cash":         "5208485880418820053",
    "folder":       "6039630677182254664",
    "add":          "5276398496008663230",
    "back_red":     "5206510891247371052",
    "coin":         "5388774339623540025",
    "letter":       "5204094761689963044",
    "cross":        "5774077015388852135",
    "nft_gift_icon":"5330131801056768633",
    "payment_icon": "5893321843149902412",
}

GIF_FILE_ID = "CgACAgEAAxkBAAFQ68hqcNBWggYy-exNThIEUlzGMqiu7AACtggAAm6_eEdToYIMGqwR1j0E"

CHANNEL_URL  = "https://t.me/notcoin"
SUPPORT_URL  = "https://t.me/NotCoinSafety"
ESCROW_URL   = "https://t.me/NotCoinEscrow"

COMMISSION = 0.01
MIN_TON_WITHDRAWAL = 2.0

LANGUAGES = {
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English",
    "ar": "🇸🇦 العربية",
    "zh": "🇨🇳 中文",
}

DEAL_TYPES = {
    "nft_gift":  "NFT-Подарок / Подарок",
    "channel":   "Канал / Чат",
    "stars":     "Звезды",
    "username":  "NFT-юзернеймы / Тег",
    "other":     "Другое",
}

PAYMENT_METHODS = {
    "ton":   "На TON-Кошелек",
    "card":  "Перевод На карту / СБП",
    "stars": "Звезды",
}

CARD_REGIONS = [
    "РФ", "Казахстан", "Украина", "Беларусь",
    "Грузия", "Молдова", "Таджикистан", "Туркменистан",
    "Германия", "Франция", "Италия", "Испания",
    "Нидерланды", "Бельгия", "Австрия", "Португалия",
    "Финляндия", "Ирландия", "Греция", "Словакия",
    "Словения", "Эстония", "Латвия", "Литва",
    "Кипр", "Мальта", "Люксембург", "США",
]
