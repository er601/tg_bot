from aiogram import types
from config import bot, dp
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.reply('Hello World')


@dp.message_handler(commands=['task1'])
async def task_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_answer = InlineKeyboardButton('Ответ', callback_data='button_call_answer')
    markup.add(button_call_answer)
    question = 'Смог решить задачу?'
    answer = [
        'Да',
        'Нет',
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Нажми на кнопу\!',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_answer')
async def quiz_2(call: types.CallbackQuery):
    await call.message.reply('''
        list1 = [1, 2, 3, 4]
        list1_copy = list1.copy()
        list1.extend(list1_copy)
        print('list1 =', list1)
    ''')


# ----------task2-----
@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Следующая Викторина', callback_data='button_call_1')
    markup.add(button_call_1)
    question = 'Сколько типов данных в питон'
    answer = [
        '2',
        '4',
        '8',
        '6'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup,
    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
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

@dp.callback_query_handler(lambda call: call.data == 'button_call_2')
async def quiz_2(call: types.CallbackQuery):
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)