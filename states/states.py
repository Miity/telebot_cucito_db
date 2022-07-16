from aiogram.dispatcher.filters.state import StatesGroup, State


class AddClientStates(StatesGroup):
    state_mode_start = State()
    state_mode_step = State()
    state_name = State()
    state_phone = State()
    state2_mode_step = State()
    state_photo = State()

class AddBoatStates(StatesGroup):
    state_mode_step = State()
    state_name = State()
    state_owner = State()
    state_photo = State()

class ShowClientStates(StatesGroup):
    state_mode_step = State()

class ChangeState(StatesGroup):
    state_change_mode = State()
    state_change_client = State()
    state_change_boat = State()