from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message


commands_router = Router()

@commands_router.message(Command('help'))
async def CmdCommnadHelp(message:Message):
    await message.answer("Help command")