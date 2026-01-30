# Epic Title: User Account Management
import mysql.connector

class UserSessionRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_account_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_user_by_email(self, email: str) -> dict:
        query = "SELECT id, email, password FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()