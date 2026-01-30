# Epic Title: User Account Management
import mysql.connector

class ProfileManagementRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_account_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_profile(self, user_id: int) -> dict:
        query = "SELECT email, first_name, last_name FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def update_profile(self, user_id: int, data: dict) -> bool:
        query = "UPDATE users SET email = %s, first_name = %s, last_name = %s WHERE id = %s"
        self.cursor.execute(query, (data['email'], data['first_name'], data['last_name'], user_id))
        self.connection.commit()
        return self.cursor.rowcount > 0