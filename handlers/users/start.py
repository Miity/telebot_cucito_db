from aiogram import types
from loader import dp
from keyboards.default.menu import keyboard_start


@dp.message_handler(text='/start')
async def command_start(message: types.Message):

    text = 'Hi {}'.format(message.from_user.full_name)+'\nYour id: {}'.format(message.from_user.id)
    await message.answer(text = text, reply_markup=keyboard_start)
