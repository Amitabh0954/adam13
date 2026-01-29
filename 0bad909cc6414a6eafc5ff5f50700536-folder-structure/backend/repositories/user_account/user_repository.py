# Epic Title: User Account Management

from typing import Optional, Dict
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

    def find_user_by_email(self, email: str) -> Optional[Dict[str, str]]:
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

    def create_password_reset_token(self, email: str, token: str) -> None:
        cursor = self.db_connection.cursor()
        query = """
        INSERT INTO password_reset_tokens (email, token, created_at) VALUES (%s, %s, NOW())
        ON DUPLICATE KEY UPDATE token = VALUES(token), created_at = VALUES(created_at)
        """
        cursor.execute(query, (email, token))
        self.db_connection.commit()

    def find_password_reset_token(self, email: str, token: str) -> Optional[Dict[str, str]]:
        cursor = self.db_connection.cursor(dictionary=True)
        query = """
        SELECT * FROM password_reset_tokens WHERE email = %s AND token = %s AND created_at > NOW() - INTERVAL 24 HOUR
        """
        cursor.execute(query, (email, token))
        token_record = cursor.fetchone()
        self.db_connection.commit()
        return token_record

    def update_password(self, email: str, new_password_hash: str) -> None:
        cursor = self.db_connection.cursor()
        query = """
        UPDATE users SET password_hash = %s WHERE email = %s
        """
        cursor.execute(query, (new_password_hash, email))
        self.db_connection.commit()

    def update_user_profile(self, email: str, profile_data: Dict[str, str]) -> None:
        cursor = self.db_connection.cursor()
        columns = ", ".join(f"{key} = %s" for key in profile_data.keys())
        values = list(profile_data.values())
        query = f"""
        UPDATE users SET {columns} WHERE email = %s
        """
        cursor.execute(query, values + [email])
        self.db_connection.commit()