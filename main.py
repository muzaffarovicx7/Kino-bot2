from aiogram.types import Message
import logging
import asyncio
from data.config import token, admin
from aiogram import Bot, Dispatcher, F, Router
from kino.kino import kino_router
from kino.kino_add import kino_admin


bot = Bot(token=token)
dp = Dispatcher()


dp.include_router(kino_router)
dp.include_router(kino_admin)





async def main():
    for id in admin:
        await bot.send_message(chat_id=id, text="Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("Tugadi!")