from aiogram import Bot, F, Router
from aiogram.types import Message
from aiogram.filters import Command


import config
from cls import Reader, enums
from cls.deep_seek import DeepSeek, DeepSeekMessage
from keyboards.reply_kb import kb_main_menu



command_router = Router()

@command_router.message(Command('start'))
async def com_start_handler(message: Message):
    reader = Reader(
        enums.ResourcePath.RESOURCE_DIR.value / enums.ResourcePath.MESSAGES_DIR.value/ enums.ResourceFileName.MAIN_MESSAGE.value)
    message_text = await reader.load()
    await message.answer(
        text=message_text,
        reply_markup=kb_main_menu()
    )

@command_router.message(Command('random'))
async def random_handler(message: Message):
    deep_seek_client = DeepSeek()
    message_list = DeepSeekMessage('random')
    await message_list.init_message()
    response = await deep_seek_client.request(message_list)

    await message.answer(
        text=response,
    )