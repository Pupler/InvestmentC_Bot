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
    db.add_user(message.from_user.id)
    
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


@dp.message(lambda message: message.text == "👤 Profile")
async def show_user_profile(message: Message):
    telegram_id = message.from_user.id
    user_data = db.get_user_profile(telegram_id)

    if user_data:
        photo = FSInputFile(IMAGES["profile_photo"])

        profile_text = (
            f"👤 <b>Your Profile</b>\n\n"
            f"🆔 <b>ID:</b> {telegram_id}\n"
            f"💰 <b>Balance:</b> ${user_data['balance']:.2f}\n"
            f"📅 <b>Registered:</b> {user_data['created_at'].strftime('%Y-%m-%d %H:%M')}"
        )
    else:
        profile_text = "❌ Profile not found"

    await message.answer_photo(
        photo=photo,
        caption=profile_text,
        reply_markup=main_kb,
        parse_mode="HTML"
    )
        


async def main():
    print("✅ Bot is started!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())