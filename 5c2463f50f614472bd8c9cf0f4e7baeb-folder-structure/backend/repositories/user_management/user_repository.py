# Epic Title: User Account Management
import mysql.connector

class UserRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_management_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def exists_by_email(self, email: str) -> bool:
        query = "SELECT COUNT(*) as count FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        return result['count'] > 0

    def create_user(self, email: str, password: str) -> int:
        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        self.cursor.execute(query, (email, password))
        self.connection.commit()
        return self.cursor.lastrowid