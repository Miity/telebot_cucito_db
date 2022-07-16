import logging
from aiogram import Dispatcher
from loader import bot
from data.config import admins_id
from keyboards.default.menu import keyboard_start

logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)


async def on_start_notify(dp:Dispatcher):
    for admin in admins_id:
        try:
            text = 'бот запущен'
            await dp.bot.send_message(chat_id=admin, text=text, reply_markup=keyboard_start )
        except Exception as e:
            print('error in "on_start_notify" \n', e)