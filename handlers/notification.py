import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

# 719370351


async def payment():
    ADMIN_ID = '719370351'
    await bot.send_message(
        chat_id=ADMIN_ID,
        text='Не забудь оплатить счёт за коммуналку!!!'
    )


async def schedular():
    aioschedule.every().friday.at('20:00').do(payment)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

