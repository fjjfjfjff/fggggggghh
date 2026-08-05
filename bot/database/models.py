import uuid
from datetime import datetime
from sqlalchemy import (
    BigInteger, String, Float, Boolean,
    DateTime, ForeignKey, Text, Enum as SAEnum
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from bot.database.engine import Base
import enum


class DealStatus(str, enum.Enum):
    PENDING    = "pending"
    ACTIVE     = "active"
    PAID       = "paid"
    COMPLETED  = "completed"
    CANCELLED  = "cancelled"
    TRANSFERRED = "transferred"
    DISPUTED   = "disputed"


class DealType(str, enum.Enum):
    NFT_GIFT  = "nft_gift"
    CHANNEL   = "channel"
    STARS     = "stars"
    USERNAME  = "username"
    OTHER     = "other"


class PaymentMethod(str, enum.Enum):
    TON   = "ton"
    CARD  = "card"
    STARS = "stars"


class UserRole(str, enum.Enum):
    SELLER = "seller"
    BUYER  = "buyer"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str | None] = mapped_column(String(64), nullable=True)
    language: Mapped[str] = mapped_column(String(8), default="ru")
    balance_rub: Mapped[float] = mapped_column(Float, default=0.0)
    balance_ton: Mapped[float] = mapped_column(Float, default=0.0)
    balance_stars: Mapped[float] = mapped_column(Float, default=0.0)
    successful_deals: Mapped[int] = mapped_column(BigInteger, default=0)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    referral_code: Mapped[str] = mapped_column(String(16), unique=True, nullable=False)
    referred_by: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    referral_bonus: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    requisites: Mapped[list["Requisite"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    seller_deals: Mapped[list["Deal"]] = relationship(foreign_keys="Deal.seller_id", back_populates="seller")
    buyer_deals: Mapped[list["Deal"]] = relationship(foreign_keys="Deal.buyer_id", back_populates="buyer")
    operations: Mapped[list["Operation"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Requisite(Base):
    __tablename__ = "requisites"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.telegram_id"), nullable=False)
    ton_wallet: Mapped[str | None] = mapped_column(String(128), nullable=True)
    card_number: Mapped[str | None] = mapped_column(String(32), nullable=True)
    card_region: Mapped[str | None] = mapped_column(String(64), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="requisites")


class Deal(Base):
    __tablename__ = "deals"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    deal_id: Mapped[str] = mapped_column(String(16), unique=True, nullable=False, default=lambda: uuid.uuid4().hex[:10].upper())
    seller_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("users.telegram_id"), nullable=True)
    buyer_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("users.telegram_id"), nullable=True)
    deal_type: Mapped[DealType] = mapped_column(SAEnum(DealType), nullable=False)
    payment_method: Mapped[PaymentMethod] = mapped_column(SAEnum(PaymentMethod), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    commission: Mapped[float] = mapped_column(Float, nullable=False)
    amount_after_commission: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[DealStatus] = mapped_column(SAEnum(DealStatus), default=DealStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    seller: Mapped["User"] = relationship(foreign_keys=[seller_id], back_populates="seller_deals")
    buyer: Mapped["User"] = relationship(foreign_keys=[buyer_id], back_populates="buyer_deals")


class Operation(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.telegram_id"), nullable=False)
    type: Mapped[str] = mapped_column(String(32), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    currency: Mapped[str] = mapped_column(String(16), nullable=False)
    deal_id: Mapped[str | None] = mapped_column(String(16), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship(back_populates="operations")
