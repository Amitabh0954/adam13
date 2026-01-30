# Epic Title: User Account Management
import mysql.connector

class PasswordRecoveryRepository:
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
        return self.cursor.fetchone()

    def update_password(self, user_id: int, hashed_password: bytes) -> bool:
        query = "UPDATE users SET password = %s WHERE id = %s"
        self.cursor.execute(query, (hashed_password, user_id))
        self.connection.commit()
        return self.cursor.rowcount > 0