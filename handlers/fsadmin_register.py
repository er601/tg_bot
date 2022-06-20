from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards import register_kb


class ShowsUserStates(StatesGroup):
    user_id = State()
    username = State()
    user_first_name = State()
    user_last_name = State()
    photo_profile = State()


async def start_register(message: types.Message):
    await bot.send_message(message.chat.id,
                     'Click on the /upload button to start registration',
                     reply_markup=register_kb.register_markup)


async def cancel_command(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.reply("State is not")
    await state.finish()
    await message.reply('States successfully canceled')


async def fsm_start(message: types.Message, state: FSMContext):
    await ShowsUserStates.user_id.set()
    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
    await ShowsUserStates.next()
    await message.reply('Send me your user name, please')


async def load_user_name(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
        if message.from_user.username == data['username']:
            await ShowsUserStates.next()
            await message.reply('Send me your first name, please')
        else:
            await message.reply('You sent not your username, please try again')


async def load_first_name(message: types.Message,
                          state: FSMContext):
    async with state.proxy() as data:
        data['user_first_name'] = message.text
    await ShowsUserStates.next()
    await message.reply('Send me your last name, please')


async def load_last_name(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['user_last_name'] = message.text
        data['photo_profile'] = message.from_user.get_profile_photos
        await message.reply(str(data))
        await state.finish()


def register_users_handler(dp: Dispatcher):
    dp.register_message_handler(start_register, commands=['start_register'])
    dp.register_message_handler(cancel_command,
                                state='*',
                                commands=['cancel'])
    dp.register_message_handler(cancel_command,
                                Text(
                                    equals='cancel',
                                    ignore_case=False),
                                state='*')
    dp.register_message_handler(fsm_start,
                                commands=['upload'],
                                state=None)
    dp.register_message_handler(fsm_start, state=ShowsUserStates.user_id)
    dp.register_message_handler(load_user_name,
                                content_types=['text'],
                                state=ShowsUserStates.username)
    dp.register_message_handler(load_first_name,
                                content_types=['text'],
                                state=ShowsUserStates.user_first_name)
    dp.register_message_handler(load_last_name,
                                content_types=['text'],
                                state=ShowsUserStates.user_last_name)
    dp.register_message_handler(load_last_name,
                                state=ShowsUserStates.photo_profile)
