# Epic Title: User Account Management

from typing import Optional
import mysql.connector
from mysql.connector import connection

class UserRepository:
    def __init__(self, db_connection: connection.MySQLConnection):
        self.db_connection = db_connection
        
    def create_user(self, email: str, password_hash: str) -> None:
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO users (email, password_hash) VALUES (%s, %s)
        """
        cursor.execute(query, (email, password_hash))
        self.db_connection.commit()

    def find_user_by_email(self, email: str) -> Optional[dict]:
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT * FROM users WHERE email = %s
        """
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        self.db_connection.commit()
        return user