# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from aiogram import executor

from magic import dp


async def start(_):
    print("Starting Bot /..... Done!")

from Handlers import startt

startt.reg_handlers(dp)


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=start)


if __name__ == '__main__':
    main()


