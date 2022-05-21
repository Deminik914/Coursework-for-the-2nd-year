# task_list_key.py
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards import task_list_key, help, start
from db import models
import datetime
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create import *


class FSMRecord(StatesGroup):
    date = State()


async def list_task(message: types.message):
    query = models.Record.select().where(models.Record.user_id == message.from_user.id)
    if query:
        records_selected = query.dicts().execute()
        answer = ""
        for task in records_selected:
            text = task["body"]
            date = task["reminder_date"]
            answer += f"\n{date}<b>  --->  </b><code>{text}</code>"
        await message.answer(f'{"Сегодня: " + str(datetime.datetime.now().strftime("%d.%m.%Y"))}\n{answer}',
                             parse_mode='html', reply_markup=task_list_key.del_all_task_key)
    else:
        await message.answer("Пусто")


async def remove_all_rec(message: types.message):
    query = models.Record.delete().where(models.Record.user_id == message.from_user.id)
    query.execute()
    await message.answer('ok')


async def del_task_by_date_start(message: types.message):
    await FSMRecord.date.set()
    await message.reply("🗓 Укажить дату (Д.М.Г)")


async def del_task_by_date(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['date'] = datetime.datetime.strptime(message.text, dateformat).strftime(dateformat)
        query = models.Record.delete().where(models.Record.reminder_date == data['date'])
        query.execute()
    except:
        await message.answer("Укажить дату задачи")
        return
    await state.finish()
    await message.answer("ok")


def regester_list_task(dp: Dispatcher):
    dp.register_message_handler(list_task, Text(equals="Список задач"))
    dp.register_message_handler(remove_all_rec, Text(equals="Удалить все записи!"))
    dp.register_message_handler(del_task_by_date_start, Text(equals="Удалить по дате"), state=None)
    dp.register_message_handler(del_task_by_date, state=FSMRecord.date)
