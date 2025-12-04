# states/user_states.py
from telebot.handler_backends import StatesGroup, State


class UserStates(StatesGroup):
    """
    Стан FSM користувача.
    """
    idle = State()                 # "нічого не чекаємо"
    waiting_for_skin_name = State()  # очікуємо, що користувач введе назву скіна