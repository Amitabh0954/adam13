# Epic Title: User Account Management
import mysql.connector
import bcrypt

class UserSessionRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_account_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_user_by_email(self, email: str) -> dict | None:
        query = "SELECT * FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        user = self.cursor.fetchone()
        return user

    def verify_password(self, stored_password: bytes, provided_password: str) -> bool:
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))