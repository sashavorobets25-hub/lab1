from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("Пошук скіна за назвою"),
        KeyboardButton("Популярні скіни"),
    )

    return kb
