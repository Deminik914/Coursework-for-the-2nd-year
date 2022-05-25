# main.py
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards import start, help


async def start_command(message: types.Message):
    await message.answer("Hello. Bot it`s work!!!", reply_markup=start.markup_start_menu)


async def back_battuon(message: types.Message):
    await message.answer("Hello. Bot it`s work!!!", reply_markup=start.markup_start_menu)


async def help_command(message: types.Message):
    await message.answer("Привет, этот бот поможет тебе не забывть про твои поставленные задачи.",
                         reply_markup=help.url_git)


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(help_command, Text(equals="Help"))
    dp.register_message_handler(back_battuon, Text(equals="Назад"))
