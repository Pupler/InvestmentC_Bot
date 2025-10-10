import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

# Bot settings
GROWTH_RATE = 0.05  # % 
GROWTH_INTERVAL = 30  # Seconds
MIN_WITHDRAWAL = 300.0 # Minimal sum that user can withdraw
START_BALANCE = 0.0 # Start balance of user

# Images
IMAGES = {
    "welcome_photo": "images/welcome.png",
    "balance_photo": "images/balance.png", 
    "deposit_photo": "images/deposit.png",
    "withdraw_photo": "images/withdraw.png",
    "growth_photo": "images/growth.png",
    "admin_photo": "images/admin.jpg"
}

# MySQL Config
MYSQL_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD")
}