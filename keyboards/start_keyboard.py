from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_kb():
    quiz_button = KeyboardButton("/quiz")
    mark_up = ReplyKeyboardMarkup(one_time_keyboard=True)

    mark_up.add(quiz_button)
    return mark_up
