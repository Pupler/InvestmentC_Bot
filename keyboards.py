from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Create buttons
profile_btn = KeyboardButton(text="👤 Profile")
invest_btn = KeyboardButton(text="💵 Invest")
withdraw_btn = KeyboardButton(text="📤 Withdraw")
support_btn = KeyboardButton(text="🖥 Support")

invest_10 = InlineKeyboardButton(text="💰 $10", callback_data="invest_10")
invest_50 = InlineKeyboardButton(text="💰 $50", callback_data="invest_50")
invest_100 = InlineKeyboardButton(text="💰 $100", callback_data="invest_100")
back_to_main = InlineKeyboardButton(text="🔙 Back", callback_data="back_to_main")


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [profile_btn],
        [invest_btn, withdraw_btn],
        [support_btn]
    ],
    resize_keyboard=True
)

invest_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [invest_10, invest_50, invest_100],
        [back_to_main]
    ]
)