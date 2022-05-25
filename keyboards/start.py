# start.py
from aiogram import types
from aiogram.types import KeyboardButton, InlineKeyboardButton

markup_start_menu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Список задач")
).add(
    KeyboardButton("➕ Добавить задачу")
).add(
    KeyboardButton("Help")
)
