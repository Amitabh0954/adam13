# Epic Title: User Account Management
import mysql.connector

class UserRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_account_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def email_exists(self, email: str) -> bool:
        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        return result['COUNT(*)'] > 0

    def get_user_by_email_and_password(self, email: str, password: str) -> dict:
        query = "SELECT id, email FROM users WHERE email = %s AND password = %s"
        self.cursor.execute(query, (email, password))
        return self.cursor.fetchone()