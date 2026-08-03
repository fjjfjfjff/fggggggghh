from aiogram.fsm.state import State, StatesGroup


class DealCreation(StatesGroup):
    choosing_role          = State()
    choosing_type          = State()
    choosing_payment       = State()
    entering_amount        = State()
    entering_description   = State()


class RequisiteStates(StatesGroup):
    entering_ton_wallet    = State()
    choosing_card_region   = State()
    entering_card_number   = State()


class WithdrawStates(StatesGroup):
    confirming             = State()
