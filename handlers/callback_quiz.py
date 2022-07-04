from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from aiogram import Dispatcher


async def answer_task1(call: types.CallbackQuery):
    await call.message.reply('''
        list1 = [1, 2, 3, 4]
        list1_copy = list1.copy()
        list1.extend(list1_copy)
        print('list1 =', list1)
    ''')


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Следующая Викторина', callback_data='button_call_2')
    markup.add(button_call_2)
    question = 'В каком году придумали питон'
    answer = [
        'В 1667 году',
        'В 1978 году',
        'В 2000 году',
        'В 1980 году',
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        reply_markup=markup,
    )


async def quiz_3(call: types.CallbackQuery):
    question = 'На каком языке написан Golang'
    answer = [
        'C++',
        'Ruby',
        'php',
        'Python'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
    )


def register_handlers_callback_quiz(dp: Dispatcher):
    dp.register_callback_query_handler(answer_task1, lambda call: call.data == 'button_call_answer')
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')

