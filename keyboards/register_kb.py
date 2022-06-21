from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

upload_button = KeyboardButton('/upload')
cancel_button = KeyboardButton('/cancel')
delete_button = KeyboardButton('/delete')
get_all_users = KeyboardButton('/users')

register_markup = ReplyKeyboardMarkup(resize_keyboard=True)

register_markup.row(
    upload_button,
    cancel_button,
    delete_button,
    get_all_users
)
