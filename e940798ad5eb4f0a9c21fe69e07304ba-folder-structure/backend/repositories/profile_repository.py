# Epic Title: User Account Management
import mysql.connector
from backend.models.user_account.profile import Profile

class ProfileRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_profile(self, user_id: int) -> dict:
        self.cursor.execute("SELECT * FROM profiles WHERE user_id = %s", (user_id,))
        return self.cursor.fetchone()

    def update_profile(self, profile: Profile) -> bool:
        query = """
        UPDATE profiles SET first_name = %s, last_name = %s, email = %s, preferences = %s
        WHERE user_id = %s
        """
        self.cursor.execute(query, (profile.first_name, profile.last_name, profile.email, profile.preferences, profile.user_id))
        self.connection.commit()
        return self.cursor.rowcount > 0