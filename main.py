from aiogram import Bot, Dispatcher

from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

import asyncio

from keyboards import main_kb
from config import BOT_TOKEN, IMAGES, GROWTH_INTERVAL, GROWTH_RATE
from database import My_SQL


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
db = My_SQL()

@dp.message(Command("start"))
async def start(message: Message):
    photo = FSInputFile(IMAGES["welcome_photo"])

    welcome_text = (
        "<b>🚀 Welcome to Investment Bot!</b>\n\n"
        f"💰 Every {GROWTH_INTERVAL} seconds: +{GROWTH_RATE * 100:.1f}% to your balance\n"
        "📈 Continuous automatic growth\n"
        "⚡ Fast and steady profits\n\n"
        "<i>💎 Invest your money and easily get profit!</i>"
    )

    await message.answer_photo(
        photo=photo,
        caption=welcome_text,
        reply_markup=main_kb,
        parse_mode="HTML"
    )



async def main():
    print("✅ Bot is started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())