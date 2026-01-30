# Epic Title: User Account Management
import mysql.connector
from backend.models.user_account.user import User
from backend.models.user_account.session import Session
from datetime import datetime, timedelta

class UserAccountRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def find_user_by_email(self, email: str) -> dict:
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone()

    def register_session(self, user_id: int, session_token: str, duration: timedelta) -> bool:
        expires_at = datetime.now() + duration
        self.cursor.execute(
            "INSERT INTO sessions (user_id, session_token, expires_at) VALUES (%s, %s, %s)", 
            (user_id, session_token, expires_at)
        )
        self.connection.commit()
        return self.cursor.rowcount > 0

    def get_session(self, session_token: str) -> dict:
        self.cursor.execute("SELECT * FROM sessions WHERE session_token = %s", (session_token,))
        return self.cursor.fetchone()

    def invalidate_session(self, session_token: str) -> bool:
        self.cursor.execute("DELETE FROM sessions WHERE session_token = %s", (session_token,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def get_invalid_attempts(self, user_id: int) -> int:
        self.cursor.execute("SELECT invalid_attempts FROM users WHERE id = %s", (user_id,))
        return self.cursor.fetchone()['invalid_attempts']

    def update_invalid_attempts(self, user_id: int, invalid_attempts: int) -> bool:
        self.cursor.execute("UPDATE users SET invalid_attempts = %s WHERE id = %s", (invalid_attempts, user_id))
        self.connection.commit()
        return self.cursor.rowcount > 0