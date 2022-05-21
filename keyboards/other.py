# main.py
from aiogram import types
from aiogram.types import KeyboardButton, InlineKeyboardButton

notification_yes_no = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Да")
).add(
    KeyboardButton("Нет")
)
