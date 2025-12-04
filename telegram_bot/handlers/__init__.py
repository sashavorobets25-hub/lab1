# handlers/__init__.py
from telebot import TeleBot

from .start import register_start_handlers
from .messages import register_message_handlers
from .callbacks import register_callback_handlers


def register_handlers(bot: TeleBot) -> None:
    """
    Центральна функція реєстрації всіх хендлерів бота.
    Викликається з bot.py.
    """
    register_start_handlers(bot)
    register_message_handlers(bot)
    register_callback_handlers(bot)
