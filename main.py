from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
import os

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

kbActions = [
    [
        types.KeyboardButton(text="Library list"),
        types.KeyboardButton(text="What is my name?"),
        types.KeyboardButton(text="Fuzz"),
        types.KeyboardButton(text="Buzz"),
        types.KeyboardButton(text="FuzzBuzz")
    ],
]

# start
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    kb = kbActions
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply("This is the best bot ever made. Mark 10 points!", reply_markup=keyboard)

#action
@dp.message_handler()
async def select_distribution(message: types.Message):
    if message.text == "Library list":
        await message.reply("I use aiogram")
    elif message.text == "What is my name?":
        await message.reply("My name is John Felix Anthony Cena Jr")
    elif message.text == "Fuzz":
        await message.reply("Buzz")
    elif message.text == "Buzz":
        await message.reply("FuzzBuzz")
    elif message.text == "FuzzBuzz":
        await message.reply("Fuzz")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

