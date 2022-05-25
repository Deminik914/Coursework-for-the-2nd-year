# bot.py
import logging
from create import dp
from handlers import add_task_fsm, main, task_list
from aiogram.utils import executor

# Настройки логгера
logging.basicConfig(
    encoding='utf-8',
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("bot.log", mode="w"),
        logging.StreamHandler()
    ]
)

main.register_handlers_start(dp)
add_task_fsm.register_handlers_add_task(dp)
task_list.regester_list_task(dp)
print("Bot run")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
