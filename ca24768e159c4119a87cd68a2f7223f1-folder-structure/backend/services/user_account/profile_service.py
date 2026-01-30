# Epic Title: User Account Management
import mysql.connector

class ProfileService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_profile(self, user_id: int) -> dict:
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = self.cursor.fetchone()
        if not user:
            return {"error": "User not found"}
        return user

    def update_profile(self, user_id: int, email: str, name: str) -> dict:
        query = "UPDATE users SET email = %s, name = %s WHERE id = %s"
        self.cursor.execute(query, (email, name, user_id))
        self.connection.commit()
        if self.cursor.rowcount == 0:
            return {"error": "No changes made or user not found"}
        return {"message": "Profile updated successfully"}