from aiogram import Bot, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import openai
import httpx

import config
from cls import Reader, enums
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
    gpt_client = openai.AsyncOpenAI(
        api_key=config.DEEP_SEEK_TOKEN,
        # http_client=httpx.AsyncClient(
        #     proxy=config.PROXY,
        # )
        base_url='https://api.deepseek.com/',
    )
    reader = Reader(
        enums.ResourcePath.RESOURCE_DIR.value / enums.ResourcePath.PROMPTS_DIR.value / enums.ResourceFileName.RANDOM_FACT.value
    )
    prompt = await reader.load()
    response = await gpt_client.chat.completions.create(
        model='deepseek-chat',
        messages=[
            {
            'role': 'system',
            'content': prompt,
            },
        ]
    )
    # print(response.choices[0])
    # print(response.choices[0].message)
    # print(response.choices[0].message.content)
    await message.answer(
        text=response.choices[0].message.content,
    )