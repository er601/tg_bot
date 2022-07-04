from config import bot, dp
from aiogram.utils import executor
from handlers import client, callback_quiz, fsadmin_register, notification, inline
from database import bot_db
import asyncio


async def on_startup(_):
    bot_db.sql_create()
    print('Bot is online')
    asyncio.create_task(notification.schedular())

client.register_handlers_client(dp)
fsadmin_register.register_users_handler(dp)
callback_quiz.register_handlers_callback_quiz(dp)
inline.register_handlers_inline(dp)


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)
