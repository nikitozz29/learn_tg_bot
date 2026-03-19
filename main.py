from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import asyncio

import config
import misc

from handlers import main_router
from resources import resource

async def start_bot():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    await resource.load()

    dp.startup.register(misc.on_start)
    dp.shutdown.register(misc.on_shutdown)

    dp.include_router(main_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass