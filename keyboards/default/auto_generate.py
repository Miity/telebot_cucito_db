from typing import Dict
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def generate_menu(dic):
    l = [[]]
    i = 0
    j = 0
    for k in dic.keys():
        b = KeyboardButton(k)
        l[i].append(b)
        j+=1
        if j == 2:
            i += 1
            j=0
            l.append([])

    generate_menu = ReplyKeyboardMarkup(l,resize_keyboard=True, input_field_placeholder='chose button')
    return generate_menu