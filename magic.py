import logging
from random import randint
from aiogram import Bot, Dispatcher
from aiogram import types

bot = Bot(token="5585109755:AAHJnTJGG9c-FBTDQDI_ORMOqpOD3WUAvw0", parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

