# add_task_fsm.py
from keyboards import start
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from db import models
from aiogram.types import ReplyKeyboardRemove
import datetime
from create import dateformat


# FSM - машина состояния
class FSMRecord(StatesGroup):
    reminder_date = State()
    body = State()


async def step_one(message: types.Message):
    await FSMRecord.reminder_date.set()
    await message.reply("🗓 Укажить дату (Д.М.Г)", reply_markup=ReplyKeyboardRemove())


async def step_two(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        try:
            if datetime.datetime.strptime(message.text,
                                          dateformat).year < datetime.date.today().year or datetime.datetime.strptime(
                message.text, dateformat).month < datetime.date.today().month:
                await message.reply("Надо смотреть в будущее")
                return
            date["reminder_date"] = message.text
        except:
            await message.reply("!!Правильно видите дату!!😡")
            return
        await FSMRecord.next()
    await message.reply("Текст")


async def step_three(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date["body"] = message.text
    async with state.proxy() as date:
        models.Record.get_or_create(
            user_id=message.from_user.id,
            body=str(date["body"]),
            reminder_date=str(date["reminder_date"])
        )
    await state.finish()
    await message.answer("Задача добавлена 👌", reply_markup=start.markup_start_menu)


def register_handlers_add_task(dp: Dispatcher):
    dp.register_message_handler(step_one, Text(equals="➕ Добавить задачу"), state=None)
    dp.register_message_handler(step_two, state=FSMRecord.reminder_date)
    dp.register_message_handler(step_three, state=FSMRecord.body)



