from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

but1 = InlineKeyboardButton('add client',callback_data='add client')
but2 = InlineKeyboardButton('add boat', callback_data='add boat')
but3 = InlineKeyboardButton('show clients info')
but4 = InlineKeyboardButton('show boats info')
but5 = InlineKeyboardButton('change mode')
but6 = InlineKeyboardButton('delete mode')

inline_keyboard_start = InlineKeyboardMarkup(row_width=3,
inline_keyboard=[
    [but1,but2]
])
