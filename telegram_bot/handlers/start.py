from telebot import TeleBot
from telebot.types import Message

from keyboards import main_menu_keyboard


def register_start_handlers(bot: TeleBot) -> None:
    """
    Реєстрація команди /start
    """

    @bot.message_handler(commands=["start"])
    def cmd_start(message: Message):
        text = (
            "👋 Привіт! Я бот для перевірки цін скінів CS2.\n\n"
            "Що я вмію:\n"
            "• 🔍 Шукати ціну скіна за назвою\n"
            "• 🔥 Показувати популярні скіни\n"
            "• 🛠 Працюю через API WhiteMarket\n\n"
            "Обери дію нижче 👇"
        )

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=main_menu_keyboard()
        )
