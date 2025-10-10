import mysql.connector
from config import MYSQL_CONFIG


class My_SQL:
    def __init__(self):
        self.connection = None
        self.connect()
        self.create_database()
        self.create_tables()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**MYSQL_CONFIG)
            print("✅ MySQL connected!")
        except Exception as e:
            print(f"❌ MySQL NOT connected! \nThe following error occured while connecting: {e}")

    def create_database(self):
        # Get cursor
        cursor = self.connection.cursor()
        
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS invest_bot")
            cursor.close()
            print("✅ Database created!")
            self.connection.database = "invest_bot"
        
        except Exception as e:
            print(f"❌ Database NOT created! \nThe following error occured while creating database: {e}")

    def create_tables(self):
        cursor = self.connection.cursor()

        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    telegram_id BIGINT UNIQUE NOT NULL,
                    balance DECIMAL(15, 2) DEFAULT 0.00,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT ,
                    type ENUM('DEPOSIT', 'WITHDRAW', 'GROWTH'),
                    amount DECIMAL(15, 2),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
        
            cursor.close()
            print("✅ Tables created!")
        
        except Exception as e:
            print(f"❌ Tables NOT created! \nThe following error occured while creating tables: {e}")




if __name__ == "__main__":
    db = My_SQL()