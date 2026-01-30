# Epic Title: User Account Management
from datetime import datetime, timedelta
import mysql.connector

class PasswordResetRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_account_db"
        )
        self.cursor = self.connection.cursor()

    def create_password_reset_request(self, user_id: int, token: str) -> None:
        expires_at = datetime.now() + timedelta(hours=24)
        query = "INSERT INTO password_resets (user_id, token, expires_at) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (user_id, token, expires_at))
        self.connection.commit()

    def get_password_reset_request(self, token: str) -> dict:
        query = "SELECT user_id, token, expires_at FROM password_resets WHERE token = %s"
        self.cursor.execute(query, (token,))
        result = self.cursor.fetchone()
        if result:
            return {'user_id': result[0], 'token': result[1], 'expires_at': result[2]}
        return None

    def delete_password_reset_request(self, token: str) -> None:
        query = "DELETE FROM password_resets WHERE token = %s"
        self.cursor.execute(query, (token,))
        self.connection.commit()