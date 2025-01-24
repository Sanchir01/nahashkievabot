from aiogram import Bot,Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart,Command

token = Bot(token="7323189846:AAF4mDhlTaz_dtU2QbAXYgzTUaZWRrnqNI0")
dp = Dispatcher()


    
@dp.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Hi')
    await message.reply('Как дела')

@dp.message(Command("help"))
async def cmd_help(message:Message):
    await message.answer("вы нажали на /help")
async def main():
    await dp.start_polling(token)

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")



