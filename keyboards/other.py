# main.py
from aiogram import types
from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

notification_yes_no = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Да")
).add(
    KeyboardButton("Нет")
)

calendar_key = InlineKeyboardMarkup().add(
    InlineKeyboardButton(text="Календарь", callback_data="calendar_start")
)