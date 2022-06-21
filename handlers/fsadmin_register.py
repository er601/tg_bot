from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from database import bot_db
from keyboards import register_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
    await ShowsUserStates.next()
    await message.reply('Send me your profile photo, please')


async def load_profile_photo(message: types.Message,
                             state: FSMContext):
    async with state.proxy() as data:
        data['photo_profile'] = message.photo[0].file_id
    await bot_db.sql_insert(state)
    await message.reply('Data saved!')
    await state.finish()


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_delete(call.data.replace('delete ', ''))
    await call.answer(text=f'{call.data.replace("delete ", "")} Deleted',
                      show_alert=True)


async def delete_data(message: types.Message):
    selected_data = await bot_db.sql_select_for_delete()
    for result in selected_data:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=result[4],
            caption=f'Account id: {result[0]}\n'
                    f'User name: {result[1]}\n'
                    f'First name: {result[2]}\n'
                    f'Last name: {result[3]}',
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(
                    f'Delete: {result[1]}',
                    callback_data=f'delete {result[0]}'
                )
            )
        )


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
    dp.register_message_handler(load_profile_photo,
                                content_types=['photo'],
                                state=ShowsUserStates.photo_profile)
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))
    dp.register_message_handler(delete_data, commands=['delete'])
