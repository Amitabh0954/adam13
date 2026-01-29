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

    def register_failed_attempt(self, email: str) -> None:
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO failed_attempts (email, attempt_time) VALUES (%s, NOW())
        """
        cursor.execute(query, (email,))
        self.db_connection.commit()

    def count_recent_failed_attempts(self, email: str, minutes: int) -> int:
        cursor = self.db_connection.cursor()
        query = """
        SELECT COUNT(*) FROM failed_attempts WHERE email = %s AND attempt_time > NOW() - INTERVAL %s MINUTE
        """
        cursor.execute(query, (email, minutes))
        count = cursor.fetchone()[0]
        return count