# create.py
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
dateformat = "%d.%m.%Y"



bot = Bot(os.getenv("TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
