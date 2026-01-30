# Epic Title: User Account Management
import mysql.connector
from backend.models.user_account.user import User
from backend.models.user_account.session import Session
from backend.models.user_account.password_reset_token import PasswordResetToken
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

    # Existing methods...

    def create_password_reset_token(self, user_id: int) -> PasswordResetToken:
        token = PasswordResetToken(user_id)
        self.cursor.execute(
            "INSERT INTO password_reset_tokens (user_id, token, expires_at) VALUES (%s, %s, %s)", 
            (token.user_id, token.token, token.expires_at)
        )
        self.connection.commit()
        return token

    def get_password_reset_token(self, token: str) -> dict:
        self.cursor.execute("SELECT * FROM password_reset_tokens WHERE token = %s", (token,))
        return self.cursor.fetchone()

    def invalidate_password_reset_token(self, token: str) -> bool:
        self.cursor.execute("DELETE FROM password_reset_tokens WHERE token = %s", (token,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def update_user_password(self, user_id: int, password_hash: str) -> bool:
        self.cursor.execute("UPDATE users SET password_hash = %s WHERE id = %s", (password_hash, user_id))
        self.connection.commit()
        return self.cursor.rowcount > 0