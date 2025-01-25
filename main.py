import os
from aiogram import Bot,Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from dotenv import dotenv_values,load_dotenv
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.user_router import user_router
load_dotenv()
config = dotenv_values(".env")
token = Bot(token = os.getenv("TOKEN"))

dp = Dispatcher()
dp.include_routers(user_router)


class user_data(StatesGroup):
    name = State()
    age = State()
    mood = State()



@dp.message(F.text == '1')
async def jbf(message:Message,state:FSMContext):
    await state.set_state(user_data.name)
    await message.answer("Как тебя зовут")

@dp.message(user_data.name)
async def name(message:Message,state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(user_data.age)
    await message.answer("Введите свой возраст")


@dp.message(user_data.age)
async def age(message:Message, state:FSMContext):
    try:
        age= int(message.text)
        await state.update_data(age = age)
        await state.set_state(user_data.mood)
        await message.answer("Как у вас дела")
    except ValueError:
        await message.answer("Введите возраст числом")
        
@dp.message(user_data.mood)
async def name(message:Message,state:FSMContext):
    try:
        mood = message.text
        data = await state.get_data()
        name = data.get("name")
        age = data.get("age")
        await message.answer(f'Привет твои данные:{name} \n{age}\n{mood}')
        await state.clear()
    except ValueError:
        await message.answer("Error data")

@dp.message(Command("help"))
async def cmd_help(message:Message):
    await message.answer("вы нажали на /help")

async def main():
    await Bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(token)

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")



