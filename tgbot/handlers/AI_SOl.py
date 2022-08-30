import asyncio

from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from tgbot.misc.Ai_for_bot import bot


async def get_AI(message: Message):
    chat_id = message.from_user.id
    await message.answer(f"Привет, {message.from_user.full_name}\n"
                         "Я мега супер искусственный интелект\n"
                         "Мне известен ответ на любой твой вопрос\n"
                         "P.S.\n"
                         "Практически любой")
    await asyncio.sleep(1)
    await message.answer("Спроси у меня что-нибудь")


async def get_message(message: Message):
    chat_id = message.chat
    in_text = ''
    in_text = message.text
    out_text = bot(in_text)
    await message.answer(out_text)


def register_user(dp: Dispatcher):
    dp.register_message_handler(get_AI, commands=["start"], state="*")
    dp.register_message_handler(get_message, state="*")
