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

    def get_user_by_email(self, email: str) -> dict:
        query = "SELECT * FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()

    def get_user_by_id(self, user_id: int) -> dict:
        query = "SELECT * FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def create_user(self, email: str, password: str):
        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        self.cursor.execute(query, (email, password))
        self.connection.commit()

    def update_password(self, user_id: int, hashed_password: str):
        query = "UPDATE users SET password = %s WHERE id = %s"
        self.cursor.execute(query, (hashed_password, user_id))
        self.connection.commit()
        
    def update_user_profile(self, user_id: int, data: dict) -> bool:
        columns = ", ".join(f"{key} = %s" for key in data.keys())
        sql = f"UPDATE users SET {columns} WHERE id = %s"
        params = list(data.values()) + [user_id]
        self.cursor.execute(sql, params)
        self.connection.commit()
        return self.cursor.rowcount > 0