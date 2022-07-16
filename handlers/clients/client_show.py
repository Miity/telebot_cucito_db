import asyncio
import json
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.menu import keyboard_start, stop_keyboard, show_clients_keyboard

from states.states import ShowClientStates
from utils.db_sqlite.commands import count_client, select_all_clients, select_boat, select_client


@dp.message_handler(text='show clients info')
async def show_clients_info(message: types.Message):
    await ShowClientStates.state_mode_step.set()
    clients = select_all_clients()
    count = count_client()
    text = 'You have ' + str(count) + ' clients:\n'
    for client in clients:
        text += '    #' + str(client.id) +' name: '+ client.name + '\n'
    text += '\nDo you want know more about client?\n'
    text += 'Print me number of client\n'
    await message.answer(text, reply_markup=stop_keyboard)


@dp.message_handler(state=ShowClientStates.state_mode_step)
async def detail_client(message: types.Message, state: FSMContext):
    if message.text == 'stop':
        await state.finish()
        await message.answer('STOP', reply_markup=keyboard_start)
    
    elif message.text == 'sent_photos':
        if await state.get_data('media'):
            media = await sent_photo(state)
            await message.answer_media_group(media=media)
            await message.answer('What next?')
        else:
            await message.answer('This client dont have boat yet.')

    elif message.text.isnumeric():
        text = await update_data(message, state)
        await message.answer(text=text, reply_markup=show_clients_keyboard)






async def sent_photo(state):
    state_data = await state.get_data()
    photos = state_data.get('media')
    media = types.MediaGroup()
    for photo in photos:
        photobit = types.InputFile(photo)
        media.attach_photo(photobit)
    return media


async def update_data(message, state):
    client, boat_id = select_client(int(message.text))
    await state.update_data(id=client.id, 
                        name=client.name, 
                        phone=client.phone, 
                        boat=boat_id)
    text = client.text_info()
    if boat_id:
        boat, boat_id = select_boat(boat_id)
        text += boat.text_info()
        if boat.media:
            photo_path = boat.list_path_to_photo()
            await state.update_data(media=photo_path)
    return text