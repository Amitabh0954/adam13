# Epic Title: User Account Management
from typing import Optional
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
        result = self.cursor.fetchone()
        return result[0] > 0

    def create_user(self, email: str, hashed_password: str) -> int:
        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        self.cursor.execute(query, (email, hashed_password))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_user_by_email(self, email: str) -> Optional[dict]:
        query = "SELECT id, email, password FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        user = None
        if result:
            user = {'id': result[0], 'email': result[1], 'password': result[2]}
        return user