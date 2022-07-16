from cgitb import text
from aiogram import types
from loader import dp
from keyboards.inline import inline_keyboard_start


@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    text = 'Do you need help'
    await message.answer(text = text, reply_markup=inline_keyboard_start)
