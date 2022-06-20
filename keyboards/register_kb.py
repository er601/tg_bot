from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

upload_button = KeyboardButton('/upload')
cancel_button = KeyboardButton('/cancel')

register_markup = ReplyKeyboardMarkup(resize_keyboard=True)

register_markup.row(
    upload_button,
    cancel_button
)
