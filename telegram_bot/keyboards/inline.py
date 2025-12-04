from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def wear_keyboard(wears: dict):
    kb = InlineKeyboardMarkup()
    for wear in wears.keys():
        kb.add(InlineKeyboardButton(wear, callback_data=f"wear_{wear}"))
    return kb


def popular_skins_keyboard():
    """6 популярних скінів з чистими callback_data"""
    kb = InlineKeyboardMarkup()

    skins = {
        "AK-47 | Redline (Field-Tested)": "popular_redline",
        "AWP | Asiimov (Field-Tested)": "popular_asiimov",
        "M4A1-S | Golden Coil (Minimal Wear)": "popular_gcoil",
        "Desert Eagle | Blaze (Factory New)": "popular_blaze",
        "Karambit | Fade (Factory New)": "popular_fade",
        "Butterfly Knife | Doppler (Minimal Wear)": "popular_doppler",
    }

    for label, callback in skins.items():
        kb.add(InlineKeyboardButton(label, callback_data=callback))

    return kb


def search_results_keyboard(matches):
    kb = InlineKeyboardMarkup()
    for item in matches:
        name = item.get("market_hash_name", "Unknown")
        safe_name = name.replace(" ", "_").replace("|", "").replace("(", "").replace(")", "")
        kb.add(InlineKeyboardButton(name, callback_data=f"skin_{safe_name}"))
    return kb
