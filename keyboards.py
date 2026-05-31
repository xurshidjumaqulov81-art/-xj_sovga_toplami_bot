from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

qualification_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ОДДИЙ ҲАМКОР")],
        [KeyboardButton(text="XJ MASTER")],
        [KeyboardButton(text="XJ MANAGER")],
        [KeyboardButton(text="XJ BRONZE")],
        [KeyboardButton(text="XJ SILVER")]
    ],
    resize_keyboard=True
)

confirm_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ТУШУНАРЛИ ✅")]
    ],
    resize_keyboard=True
)
