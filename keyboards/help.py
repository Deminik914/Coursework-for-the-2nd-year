# help.py
from aiogram import types
from aiogram.types import KeyboardButton, InlineKeyboardButton

url_git = types.InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='GitHub', url='https://github.com/Deminik914/bot3')
)
