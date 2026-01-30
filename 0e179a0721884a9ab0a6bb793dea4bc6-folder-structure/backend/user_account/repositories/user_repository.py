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
        self.cursor = self.connection.cursor()

    def is_email_taken(self, email: str) -> bool:
        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        count = self.cursor.fetchone()[0]
        return count > 0

    def create_user(self, email: str, hashed_password: bytes) -> int:
        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        self.cursor.execute(query, (email, hashed_password))
        self.connection.commit()
        return self.cursor.lastrowid