from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ChatAction


from cls.deep_seek import DeepSeek, DeepSeekMessage
from keyboards.reply_kb import kb_main_menu
from resources import resource



command_router = Router()

@command_router.message(Command('start'))
async def com_start_handler(message: Message, bot: Bot):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=resource.images['main'],
        caption=resource.messages['main'],
        reply_markup=kb_main_menu(),
    )

@command_router.message(Command('random'))
async def random_handler(message: Message, bot: Bot):
    await bot.send_chat_action(
        chat_id=message.from_user.id,
        action=ChatAction.TYPING,
    )
    deep_seek_client = DeepSeek()
    message_list = DeepSeekMessage(resource.prompts['random'])
    response = await deep_seek_client.request(message_list)
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=resource.images['random'],
        caption=response,
    )