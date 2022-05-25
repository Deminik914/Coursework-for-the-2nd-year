# task_list_key.py
from aiogram import types
from aiogram.types import KeyboardButton, InlineKeyboardButton

del_all_task_key = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Удалить все записи!")
).add(
    KeyboardButton("Удалить по дате")
).add(
    KeyboardButton("Назад")
)
