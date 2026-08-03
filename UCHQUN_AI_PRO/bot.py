import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from config import BOT_TOKEN
from database import add_user

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Signal"), KeyboardButton(text="💎 VIP")],
        [KeyboardButton(text="👤 Profil"), KeyboardButton(text="📢 Reklama")],
        [KeyboardButton(text="⚙️ Sozlamalar")]
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def start(message: Message):
    add_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username
    )

    await message.answer(
        f"""👋 Assalomu alaykum, {message.from_user.first_name}!

🤖 UCHQUN AI PRO

📈 Pocket Option AI Signal Bot

✅ 20+ Forex
✅ 20+ OTC
✅ 8 ta indikator
✅ AI Signal
""",
        reply_markup=menu
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
