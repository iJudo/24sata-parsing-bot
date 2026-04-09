from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db import get_unsent_news, mark_as_sent
import asyncio

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def send_news():
    for new in get_unsent_news():
        news_id, img, title, link, description = new
        try:
            await bot.send_photo(
                chat_id=CHANNEL_ID, photo=img,
                caption=f"<b>{title}</b>\n\n<blockquote>{description}</blockquote>\n\n<a href='https://www.24sata.hr{link}'>Web stranica</a>",
                parse_mode="HTML")
            mark_as_sent(news_id)
        except Exception as e:
            print(f"Ошибка: {e}")
        break

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_news, "interval", seconds=5)
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
