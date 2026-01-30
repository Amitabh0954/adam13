# Epic Title: User Account Management
import mysql.connector
import json

class ProfileRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_account_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def email_exists(self, user_id: int, email: str) -> bool:
        query = "SELECT COUNT(*) FROM users WHERE email = %s AND id != %s"
        self.cursor.execute(query, (email, user_id))
        result = self.cursor.fetchone()
        return result['COUNT(*)'] > 0

    def update_profile(self, user_id: int, name: str, email: str, preferences: dict) -> bool:
        query = "UPDATE users SET name = %s, email = %s, preferences = %s WHERE id = %s"
        self.cursor.execute(query, (name, email, json.dumps(preferences), user_id))
        self.connection.commit()
        return self.cursor.rowcount > 0