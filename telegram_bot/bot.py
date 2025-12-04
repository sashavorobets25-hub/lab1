import os
from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from dotenv import load_dotenv

# Завантажуємо .env
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не знайдено у .env!")

from handlers import register_handlers

state_storage = StateMemoryStorage()
bot = TeleBot(TOKEN, state_storage=state_storage)

register_handlers(bot)

def main():
    print("Bot is running...")
    bot.infinity_polling(skip_pending=True)

if __name__ == "__main__":
    main()
