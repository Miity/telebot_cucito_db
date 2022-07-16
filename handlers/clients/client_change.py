from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.auto_generate import generate_menu
from loader import dp
from states.states import  ChangeState
from utils.db_sqlite.commands import select_all_boats, select_all_clients, select_boat, select_client
from keyboards.default.menu import stop_keyboard, keyboard_start, change_mode


@dp.message_handler(text='change mode')
async def start_change_mode(message: types.Message):
    await ChangeState.state_change_mode.set()
    await message.answer('What do you want to change?', reply_markup=change_mode)


@dp.message_handler(state=ChangeState.state_change_mode)
async def which_client(message: types.Message, state: FSMContext):
    if message.text == 'stop':
        await state.finish()
        text = 'STOP'
        await message.answer(text, reply_markup=keyboard_start)

    if message.text == 'client':
        await ChangeState.state_change_client.set()
        clients = select_all_clients()
        text = ''
        for client in clients:
            text += '#' + str(client.id) + ' Name: ' + client.name +'\n'
        text += 'Type me number of client'
        await message.answer(text, reply_markup=stop_keyboard)
    elif message.text == 'boat':
        await ChangeState.state_change_boat.set()
        boats = select_all_boats()
        text = ''
        for boat in boats:
            text += '#' + str(boat.id) + ' Name: ' + boat.name +'\n'
        text += 'Type me number of boat'
        await message.answer(text, reply_markup=stop_keyboard)
    else:
        text = 'Choose from button'
        await message.answer(text)



@dp.message_handler(state=ChangeState.state_change_client, text='name')
async def change_client(message: types.Message, state: FSMContext):
    pass


@dp.message_handler(state=ChangeState.state_change_client)
async def change_client(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if 'id' not in data:
        client = select_client(int(message.text))
        dataCl = client[0].get_data()
        await state.update_data(dataCl)
        print(client[0].get_data())
        text = client[0].text_info()
        text += '\n\n Choose what you whant change?'
        print(type(dataCl))
        await message.answer(text, reply_markup=generate_menu(dataCl))


@dp.message_handler(state=ChangeState.state_change_boat)
async def change_boat(message: types.Message, state: FSMContext):
    boat = select_boat(int(message.text))
    state.update_data(boat[0].get_data())