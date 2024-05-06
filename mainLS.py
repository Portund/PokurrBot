import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime

API_TOKEN = '6990432870:AAEcEtFtR9yJUQF-bDKJz82PCOuPXl2ZLVo'

bot = Bot(token=API_TOKEN)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

global chat_id
chat_id = None

predefined_message = "Привет! Который час? Время покурить!"
stop_message = "Выключаюсь..."

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет, отсчет времени пошел.")
    await send_message_loop(bot, message.from_user.id)

@dp.message_handler(commands=['stop'])
async def stop_command(message: types.Message):
    await message.reply(stop_message)
    global stop_loop
    stop_loop = True

async def send_message_loop(bot: Bot, user_id: int):
    global stop_loop
    stop_loop = False
    while True:
        if stop_loop:
            break
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        predefined_message = f"Время уже: {current_time}, а ты еще не осуществил покур?!"
        await bot.send_message(user_id, predefined_message)
        await asyncio.sleep(10)

if __name__ == '__main__':
    executor.start_polling(dp)
