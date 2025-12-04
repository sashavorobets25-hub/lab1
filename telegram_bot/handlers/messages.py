import requests
from telebot import TeleBot
from telebot.types import Message
import os
from dotenv import load_dotenv

load_dotenv()

WHITEMARKET_PRICES_URL = os.getenv("WHITEMARKET_PRICES_URL")

from keyboards import (
    main_menu_keyboard,
    popular_skins_keyboard,
    wear_keyboard,
)

# ===================== API =====================

import json
import os

CACHE_FILE = "prices_cache.json"

def load_prices():
    # спочатку пробуємо завантажити онлайн
    try:
        resp = requests.get(WHITEMARKET_PRICES_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        # якщо відповідь НЕ пуста — оновлюємо кеш
        if isinstance(data, list) and len(data) > 0:
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            return data

    except:
        pass

    # fallback → пробуємо завантажити кеш
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    # якщо нічого немає → повертаємо пустий
    return []

def search_items_by_name(items, query):
    query = query.lower()
    return [
        i for i in items
        if query in i.get("market_hash_name", "").lower()
    ]


def group_by_wear_strict(items):
    """Групує тільки однакову модель (ніж, рукавиці, пістолет)."""
    # 1. Отримати weapon_name першого збігу
    first = items[0]["market_hash_name"]
    weapon_name = first.split("|")[0].strip().lower()

    wear_map = {}

    for item in items:
        name = item["market_hash_name"]

        # 2. Перевіряємо чи weapon_name співпадає
        current_weapon = name.split("|")[0].strip().lower()
        if current_weapon != weapon_name:
            continue  # відкидаємо рукавиці якщо шукали ніж

        # 3. Витягуємо wear
        if "(" in name and ")" in name:
            wear = name.split("(")[-1].replace(")", "").strip()
            wear_map[wear] = item

    return wear_map

def format_price_message(item):
    name = item.get("market_hash_name", "Unknown")
    price = float(item.get("price", 0))
    count = item.get("market_product_count", "—")
    link = item.get("market_product_link", "—")

    return (
        f"🎯 *{name}*\n\n"
        f"💰 Ціна: *{price:.2f}$*\n"
        f"📦 Лотів: *{count}*\n"
        f"🔗 {link}"
    )


# ===================== Handlers =====================

def register_message_handlers(bot: TeleBot):

    # --- ПОШУК ---
    @bot.message_handler(func=lambda m: m.text and "Пошук" in m.text)
    def handle_search(message: Message):
        bot.send_message(
            message.chat.id,
            "Введи назву скіна (частково або повністю):"
        )
        bot.user_state = "awaiting_name"

    # --- ПОПУЛЯРНІ СКІНИ ---
    @bot.message_handler(func=lambda m: m.text and "Популярні" in m.text)
    def handle_popular(message: Message):
        bot.user_state = None
        bot.send_message(
            message.chat.id,
            "Ось популярні скіни:",
            reply_markup=popular_skins_keyboard()
        )

    # --- ОБРОБКА ВВЕДЕНОГО ТЕКСТУ ---
    @bot.message_handler(content_types=["text"])
    def handle_text(message: Message):

        # Якщо бот чекає назву
        if getattr(bot, "user_state", None) == "awaiting_name":
            bot.user_state = None

            bot.send_message(message.chat.id, "🔎 Шукаю...")

            items = load_prices()
            matches = search_items_by_name(items, message.text)

            if not matches:
                bot.send_message(
                    message.chat.id,
                    "❌ Скін не знайдено.",
                    reply_markup=main_menu_keyboard()
                )
                return

            # Групуємо за зношуванням
            wear_variants = group_by_wear_strict(matches)


            if len(wear_variants) == 1:
                # Один варіант — показуємо одразу
                item = list(wear_variants.values())[0]
                bot.send_message(
                    message.chat.id,
                    format_price_message(item),
                    parse_mode="Markdown",
                    reply_markup=main_menu_keyboard()
                )
                return

            # Показати кнопки зношування
            bot.send_message(
                message.chat.id,
                "Оберіть зношування:",
                reply_markup=wear_keyboard(wear_variants)
            )
            bot.wear_variants = wear_variants
            bot.user_state = "selecting_wear"
            return

        # Нормальний fallback
        bot.send_message(
            message.chat.id,
            "Скористайся меню нижче:",
            reply_markup=main_menu_keyboard()
        )

