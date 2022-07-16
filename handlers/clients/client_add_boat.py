from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import add_boat_keyboard, keyboard_start, save_photo_keyboard
from loader import dp

from states.states import AddClientStates
from utils.db_sqlite.commands import add_boat


async def add_boat_start(message: types.Message):
    await AddClientStates.state2_mode_step.set()
    await message.answer('Choose wich parrametr you want. to add by buttons', reply_markup=add_boat_keyboard)


@dp.message_handler(state=AddClientStates.state2_mode_step)
async def step_answer(message: types.Message,  state: FSMContext):
    if message.text == 'stop':
        await state.finish()
        await message.answer('STOP', reply_markup=keyboard_start)
    
    elif message.text == 'photo':
        await AddClientStates.state_photo.set()
        await message.answer('sent me photo', reply_markup=save_photo_keyboard)

    elif message.text == 'save_boat':
        data =  await state.get_data()
        if 'media' in data:
            from media import save_photos
            media = await save_photos(data['media'], data['name'])
            data['media'] = media 
        from handlers.clients.client_add import add_client_start
        await add_client_start(message)


@dp.message_handler(text =['save_photo'], state=AddClientStates.state_photo)
@dp.message_handler(content_types=['photo', 'document'], state=AddClientStates.state_photo)
async def set_photo(message: types.Message, state: FSMContext):
    if message.text == 'save_photo':
        await add_boat_start(message)

    data = await state.get_data()
    try:
        list_photo=data['media']
    except Exception as e:
        print(e)
        list_photo = []
    if message.photo:
        list_photo.append({'file_id':message.photo[-1].file_id})
    elif message.document:
        list_photo.append({'file_id':message.document.file_id})
    await state.update_data(media = list_photo)