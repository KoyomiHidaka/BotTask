import re
import time

import surrogates
from aiogram import types, Dispatcher, Bot
from magic import bot
from aiogram import filters






async def start(message: types.message):
    hello = surrogates.decode("	\ud83d\udc4b")
    back = surrogates.decode("	\u2728")
    await message.answer(f"{hello}")
    await message.answer(f"Я могу отправить тебе расписание на определенный день нажми на /Run или отправь мне этот смайлик - {back} (ВАЖНО!: после выбора дня внизу появится кнопочка со смайликом, нажми на нее прежде чем выбирать 2 день)")
    # смайлик красного восклицательного знака


async def keyboard(message: types.message):
    inlinekey = types.InlineKeyboardMarkup()
    inlinekey.add(types.InlineKeyboardButton("Monday", callback_data='Monday'))
    inlinekey.add(types.InlineKeyboardButton("Tuesday", callback_data='Tuesday'))
    inlinekey.add(types.InlineKeyboardButton("Wednesday", callback_data='Wednesday'))
    inlinekey.add(types.InlineKeyboardButton("Thursday", callback_data='Thursday'))
    inlinekey.add(types.InlineKeyboardButton("Friday", callback_data='Friday'))
    back = surrogates.decode("	\u2728")
    await message.answer(f"What day?{back}", reply_markup=inlinekey)


async def keyboardd(message: types.message):
    inlinekey = types.InlineKeyboardMarkup()
    inlinekey.add(types.InlineKeyboardButton("Monday", callback_data='Monday'))
    inlinekey.add(types.InlineKeyboardButton("Tuesday", callback_data='Tuesday'))
    inlinekey.add(types.InlineKeyboardButton("Wednesday", callback_data='Wednesday'))
    inlinekey.add(types.InlineKeyboardButton("Thursday", callback_data='Thursday'))
    inlinekey.add(types.InlineKeyboardButton("Friday", callback_data='Friday'))

    await message.answer(f"What day? {back}", reply_markup=inlinekey)


async def monday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    back = surrogates.decode("	\u2728")
    await bot.answer_callback_query(callback_query.id, text=f"{back} Monday - second week {back}", show_alert=True)
    await bot.send_message(callback_query.from_user.id, "Средства создания Web-приложений (лек.) Нурпеисова Ж.С., аға оқ. ZOOM at 10:00 - 10:50")
    await bot.send_message(callback_query.from_user.id, "Мультимедиа технологии (лек.) Сарина А.Ж., ст.пр. ZOOM at 12:00 - 12:50")
    await bot.send_message(callback_query.from_user.id, "Технология .NET программирования (лек.) Сарина А.Ж., ст.пр. ZOOM at 1:00 - 1:50")
    await bot.send_message(callback_query.from_user.id, "Модели и методы управления (лек.) Кузенбаева А.А., ст.пр. ZOOM at 2:00 - 2:50", reply_markup=retk)
back = surrogates.decode("\u2728")


async def tuesday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    await bot.answer_callback_query(callback_query.id, text=f"{back} Tuesday - second week {back}", show_alert=True)
    await bot.send_message(callback_query.from_user.id, "Профессиональный казахский язык (пр.) Кузенбаева А.А., ст.пр. 213/2 at 1:00 - 1:50")
    await bot.send_message(callback_query.from_user.id, "Академическое деловое письмо (лекция) Баяхметова А.А., ас.проф. 106/2	at 2:00 - 2:50", reply_markup=retk)


async def wednesday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    await bot.answer_callback_query(callback_query.id, text=f"{back} Wednesday - second week {back}", show_alert=True)
    await bot.send_message(callback_query.from_user.id, "Физическая культура at 11:00 - 12:50")
    await bot.send_message(callback_query.from_user.id, "Профессиональный казахский язык (пр.) Кузенбаева А.А., ст.пр. 213/2 at 2:00 - 3:50")
    await bot.send_message(callback_query.from_user.id, "Мультимедиа технологии (пр.) Сарина А.Ж., ст.пр. 313/2 at 4:00 - 4:50", reply_markup=retk)


async def thursday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    await bot.answer_callback_query(callback_query.id, text=f"{back} Thursday - second week {back}", show_alert=True)
    await bot.send_message(callback_query.from_user.id, "Академическое деловое письмо (пр.) Баяхметова А.А., ас.проф. 307/2 at 2:00 - 2:50")
    await bot.send_message(callback_query.from_user.id, "Технология .NET программирования (лаб.) Сарина А.Ж., ст.пр. 241/2 at 3:00 - 4:50")
    await bot.send_message(callback_query.from_user.id, "Мультимедиа технологии (лаб.) Сарина А.Ж., ст.пр. 241/2 at 5:00 - 6:50", reply_markup=retk)


async def friday2(callback_query: types.CallbackQuery):
    retk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = surrogates.decode("	\u2728")
    b = [f"{back}"]
    retk.add(*b)
    await bot.answer_callback_query(callback_query.id, text=f"{back} Friday - second week {back}", show_alert=True)
    await bot.send_message(callback_query.from_user.id, "Модели и методы управления (пр.) Кузенбаева А.А., ст.пр. 312/2 at 9:00 - 10:50")
    await bot.send_message(callback_query.from_user.id, "Средства создания Web-приложений (пр.) Нурпеисова Ж.С., аға оқ. 241/2 at 11:00 - 12:50", reply_markup=retk)


def reg_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(keyboard, text=["/Run", f"{back}"])
    dp.register_callback_query_handler(monday2, text="Monday")
    dp.register_callback_query_handler(tuesday2, text="Tuesday")
    dp.register_callback_query_handler(wednesday2, text="Wednesday")
    dp.register_callback_query_handler(thursday2, text="Thursday")
    dp.register_callback_query_handler(friday2, text="Friday")
