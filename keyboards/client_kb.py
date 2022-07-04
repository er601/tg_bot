from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = KeyboardButton('/start')
help_button = KeyboardButton('/help')
task1_button = KeyboardButton('/task1')
quiz_button = KeyboardButton('/quiz1')
location_button = KeyboardButton('/Share Location',
                                 request_location=True)
info_button = KeyboardButton('/Share Info',
                             request_contact=True)
start_register = KeyboardButton('/start_register')


start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_markup.row(
    start_button,
    help_button,
)

help_markup.row(
    task1_button,
    quiz_button,
    location_button,
    info_button,
    start_register
)
