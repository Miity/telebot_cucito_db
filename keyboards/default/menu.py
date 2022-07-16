from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


boat = KeyboardButton('boat')
name = KeyboardButton('name')
phone = KeyboardButton('phone')
photo = KeyboardButton('photo')
owner = KeyboardButton('owner')
save_client = KeyboardButton('save_client')
save_boat = KeyboardButton('save_boat')
stop =  KeyboardButton('stop')
sent_photos = KeyboardButton('sent_photos')
save_photos =KeyboardButton('save_photo')


save_photo_keyboard = ReplyKeyboardMarkup([
    [save_photos],
],resize_keyboard=True, input_field_placeholder='chose button')

stop_keyboard=ReplyKeyboardMarkup([
    [stop],
],resize_keyboard=True, input_field_placeholder='chose button')

show_clients_keyboard = ReplyKeyboardMarkup([
    [sent_photos],
    [stop]
],resize_keyboard=True, input_field_placeholder='chose button')

add_client_keyboard = ReplyKeyboardMarkup([
    [name,phone],
    [boat],
    [save_client],
    [stop]
],resize_keyboard=True, input_field_placeholder='chose button')

add_boat_keyboard = ReplyKeyboardMarkup([
    [photo],
    [save_boat],
    [stop]
],resize_keyboard=True, input_field_placeholder='chose button')


change_mode = ReplyKeyboardMarkup([
            [KeyboardButton('client'), KeyboardButton('boat')],
            [KeyboardButton('stop')]
            ],resize_keyboard=True, input_field_placeholder='chose button')


add_client = KeyboardButton('add client')
add_boat = KeyboardButton('add boat')
show_clients = KeyboardButton('show clients info')
show_boats = KeyboardButton('show boats info')
change_mode = KeyboardButton('change mode')
delete_mode = KeyboardButton('delete mode')

keyboard_start = ReplyKeyboardMarkup([
    [add_client],
    [show_clients],
    #[change_mode, delete_mode]
],resize_keyboard=True, input_field_placeholder='chose button')