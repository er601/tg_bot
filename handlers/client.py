from config import bot
from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from database import bot_db
from keyboards import client_kb


async def hello(message: types.Message):
    await message.reply('Hello World')
    await bot.send_message(message.chat.id,
                           'Hello im your first bot',
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await bot.send_message(message.chat.id,
                           f'Привет {message.from_user.first_name}! 😄😄😄\n'
                           f'У меня есть несколько команд: \n'
                           f'1. /start Эта команда приветствует тебя 😄😄😄 \n'
                           f'2. /help Эта команда помогает тебе с навигацией \n'
                           f'3. /task1 Эта команда для первой задачи (вопроса), '
                           f' если не смог ответить, то наджи на кнопу *ОТВЕТ* \n'
                           f'4. /quiz1 Эта команда для викторин,'
                           f' Нажми на кнопку *Следующая Викторина* чтобы перейти на следующий вопрос \n'
                           f'5. /Share Location '
                           f'Этой командой можете поделиться местоположением или информацией о себе \n'
                           f'6. /Share Info Этой командой вы можете поделиться своим номером. \n'
                           f'7. /start_register С помощью этой команды вы сможете зарегистрироваться \n'
                           f'8. /users С помощью этой команды вы сможете увидеть полный список пользователей',
                           reply_markup=client_kb.help_markup
                           )


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


async def get_all_users(message: types.Message):
    await bot_db.sql_select(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(task_1, commands=['task1'])
    dp.register_message_handler(quiz_1, commands=['quiz1'])
    dp.register_message_handler(get_all_users, commands=['users'])
