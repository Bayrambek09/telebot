import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from aiogram.fsm.context import FSMContext
from state import xisoblovchi as US
from button import *

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('start'))
async def CommandStart(message: Message):
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!", reply_markup=menu)


@dp.message(F.text == '')
async def start_(message: Message, state: FSMContext):
    await state.set_state(US.ism_k)
    await message.answer(text='')


@dp.message(US.ism_k)
async def get_bbb(message: Message, state: FSMContext):
    bbb= message.text
    await state.update_data()
    await message.answer(text='')
    await state.set_state(US.Yosh_k)


@dp.message(US.Yosh_k)
async def get_yosh(message: Message, state: FSMContext):
    = message.text
    await state.update_data()
    await message.answer(text='')
    await state.set_state(US.Til_k)


@dp.message(US.Til_k)
async def get_til(message: Message, state: FSMContext):
     = message.text
    await state.update_data()
    await message.answer(text='')
    await state.set_state(US.Tel_k)


@dp.message(US.Tel_k)
async def get_tel(message: Message, state: FSMContext):
     = message.text
    await state.update_data()
    await message.answer(text='')
    await state.set_state(US.Vil_k)


@dp.message(US.Vil_k)
async def get_(message: Message, state: FSMContext):
    = message.text
    await state.update_data()
    user_data = await state.get_data()
    = user_data.get('')
    = user_data.get('')
   = user_data.get('')
     = user_data.get('')
     = user_data.get('')

    await message.answer(text=f": {}\n: {}\n: {}\n: {}\n: {}")
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except Exception as e:
        print(f"Xatolik: {e}")
