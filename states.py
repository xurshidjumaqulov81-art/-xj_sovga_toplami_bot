from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    full_name = State()
    xj_id = State()
    qualification = State()
    phone = State()
    address = State()
