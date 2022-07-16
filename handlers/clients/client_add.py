from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.db_sqlite.schemas.client import Client
from .client_add_boat import add_boat_start

from keyboards.default.menu import add_client_keyboard, keyboard_start
from loader import dp

from states.states import AddClientStates
from utils.db_sqlite.commands import add_boat, add_client
from utils.db_sqlite.base import session


@dp.message_handler(state=AddClientStates.state_mode_start)
@dp.message_handler(text='add client')
async def add_client_start(message: types.Message):
    print('add_client_start')
    await AddClientStates.state_mode_step.set()
    await message.answer('Choose wich parrametr you want. to add by buttons', reply_markup=add_client_keyboard)


@dp.message_handler(state=AddClientStates.state_mode_step)
async def step_answer(message: types.Message,  state: FSMContext):
    await state.update_data(state_mode_step=message.text)
    if message.text == 'name':
        await AddClientStates.state_name.set()
        await message.answer('type name', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'phone':
        await AddClientStates.state_phone.set()
        await message.answer('type phone', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == 'boat':
        data = await state.get_data()
        if 'name' in data:
            await add_boat_start(message)
        else:
            await AddClientStates.state_mode_start.set()
            await message.answer('I need name')
            await add_client_start()
    elif message.text == 'stop':
        from keyboards.default.menu import keyboard_start
        await state.finish()
        text = 'STOP'
        await message.answer(text, reply_markup=keyboard_start)

    # save in database
    elif message.text == 'save_client':
        await save_client(message,state)


@dp.message_handler(state=AddClientStates.state_name)
async def set_name(message: types.Message, state: FSMContext):
    await state.update_data(name = message.text)
    await add_client_start(message)


@dp.message_handler(state=AddClientStates.state_phone)
async def set_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone = message.text)
    await add_client_start(message)






async def save_client(message, state):
    data =  await state.get_data()
    if 'name' not in data:
        await message.answer('I need know the name')
        await add_client_start(message)
    
    if 'media' in data:
            from media import save_photos
            media = await save_photos(data['media'], data['name'])
            data['media'] = media 

    if add_client(data):
        sess = session()
        client_id = sess.query(Client).filter(Client.name == data['name']).first().id
        if 'media' in data:
            data['owner_id'] = client_id
            add_boat(data)
        sess.close()
        text = 'New Client added\n    Name: {}\n    Phone:{}'.format(data.get('name'), data.get('phone'))
        await message.answer(text, reply_markup=keyboard_start)
        await state.finish()
    else:
        text = 'Something went wrong'
        await message.answer(text)
        await add_client_start(message)