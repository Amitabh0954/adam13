# Epic Title: User Account Management
import mysql.connector

class ProfileRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_account_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_profile(self, user_id: int) -> dict | None:
        query = "SELECT * FROM profiles WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()

    def update_profile(self, user_id: int, data: dict) -> bool:
        fields = ', '.join(f"{key} = %s" for key in data.keys())
        values = list(data.values())
        values.append(user_id)
        query = f"UPDATE profiles SET {fields} WHERE user_id = %s"
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.rowcount > 0