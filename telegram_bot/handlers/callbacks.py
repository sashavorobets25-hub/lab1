import io
import matplotlib.pyplot as plt
from telebot import TeleBot
from telebot.types import CallbackQuery

from handlers.messages import (
    load_prices,
    search_items_by_name,
    group_by_wear_strict,
    format_price_message
)

from keyboards import (
    wear_keyboard,
    main_menu_keyboard,
)


POPULAR_MAP = {
    "popular_redline": "AK-47 | Redline",
    "popular_asiimov": "AWP | Asiimov",
    "popular_gcoil": "M4A1-S | Golden Coil",
    "popular_blaze": "Desert Eagle | Blaze",
    "popular_fade": "Karambit | Fade",
    "popular_doppler": "Butterfly Knife | Doppler",
}


def register_callback_handlers(bot: TeleBot):

    # ===================== Популярні =====================
    @bot.callback_query_handler(func=lambda c: c.data.startswith("popular_"))
    def callback_popular(call: CallbackQuery):
        bot.answer_callback_query(call.id)

        key = call.data
        if key not in POPULAR_MAP:
            bot.send_message(call.message.chat.id, "❌ Не знайдено.")
            return

        search_name = POPULAR_MAP[key]

        items = load_prices()
        matches = search_items_by_name(items, search_name)

        if not matches:
            bot.send_message(call.message.chat.id, "❌ Не знайдено.")
            return

        wears = group_by_wear_strict(matches)
        bot.wear_variants = wears
        bot.user_state = "selecting_wear"

        bot.send_message(
            call.message.chat.id,
            f"Оберіть зношування:\n{search_name}",
            reply_markup=wear_keyboard(wears)
        )

    # ===================== Обробка wear_* =====================
    @bot.callback_query_handler(func=lambda c: c.data.startswith("wear_"))
    def callback_wear(call: CallbackQuery):
        bot.answer_callback_query(call.id)

        wear = call.data[len("wear_"):]
        item = bot.wear_variants.get(wear)

        if not item:
            bot.send_message(call.message.chat.id, "❌ Помилка вибору.")
            return

        bot.send_message(
            call.message.chat.id,
            format_price_message(item),
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard()
        )

    # ===================== Графік =====================
    @bot.callback_query_handler(func=lambda c: c.data == "wear_chart")
    def callback_wear_chart(call: CallbackQuery):
        bot.answer_callback_query(call.id)

        variants = getattr(bot, "wear_variants", {})
        if not variants:
            bot.send_message(call.message.chat.id, "❌ Немає даних.")
            return

        names = list(variants.keys())
        prices = [float(v.get("price", 0)) for v in variants.values()]

        plt.figure()
        plt.bar(names, prices)
        plt.title("Порівняння цін по зношуванню")
        plt.xlabel("Wear")
        plt.ylabel("Price $")
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)

        bot.send_photo(call.message.chat.id, buf)
