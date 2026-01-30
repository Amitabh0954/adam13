# Epic Title: User Account Management
import mysql.connector
from datetime import datetime

class PasswordResetRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_management_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def create_reset_token(self, user_id: int, token: str, expires_at: datetime):
        query = "INSERT INTO password_resets (user_id, token, expires_at) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (user_id, token, expires_at))
        self.connection.commit()

    def get_reset_entry_by_token(self, token: str) -> dict:
        query = "SELECT * FROM password_resets WHERE token = %s"
        self.cursor.execute(query, (token,))
        return self.cursor.fetchone()

    def delete_reset_entry(self, token: str):
        query = "DELETE FROM password_resets WHERE token = %s"
        self.cursor.execute(query, (token,))
        self.connection.commit()