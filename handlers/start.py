from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot
from aiogram import types, Dispatcher
from database.sql_commands import DataBase
from const import START_MENU_TEXT
from keyboards.start_keyboard import start_kb


async def start_button(message: types.Message):
    print(message)
    DataBase().sql_insert_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    with open(r"C:\pythonProjects\media\botlogo.jpeg", "rb") as photo:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=START_MENU_TEXT,
            reply_markup=await start_kb()
        )


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Следуюшая Викторина",
        callback_data="button_call_1"
    )
    markup.add(button_call_1)

    question = "Who is better"
    options = [
        "Ilon Mask",
        "Daniel",
        "Lius Torvalds",
        "Guido Van Rossum"
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        is_anonymous=False,
        type="quiz",
        correct_option_id=1,
        reply_markup=markup
    )


async def quiz_2(call: types.CallbackQuery):
    question = "Who invented Linux"
    option = [
        "Chepolinko",
        "Mario",
        "Linus Torvalds",
        "Lannister"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=option,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='This is so easy not gonna explain',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
