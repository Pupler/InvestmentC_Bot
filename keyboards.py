from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Create buttons
profile_btn = KeyboardButton(text="👤 Profile")
invest_btn = KeyboardButton(text="💵 Invest")
withdraw_btn = KeyboardButton(text="📤 Withdraw")
support_btn = KeyboardButton(text="🖥 Support")


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [profile_btn],
        [invest_btn, withdraw_btn],
        [support_btn]
    ],
    resize_keyboard=True
)