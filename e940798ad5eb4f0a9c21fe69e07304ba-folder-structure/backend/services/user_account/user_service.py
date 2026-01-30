# Epic Title: User Account Management
from backend.models.user_account.user import User
import mysql.connector

class UserService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def register_user(self, email: str, password: str) -> dict:
        if not User.validate_email(email):
            return {"error": "Invalid email format"}
        if not User.validate_password(password):
            return {"error": "Password does not meet security criteria"}

        self.cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        if self.cursor.fetchone():
            return {"error": "Email is already registered"}

        user = User(id=None, email=email, password=password)
        self.cursor.execute(
            "INSERT INTO users (email, password_hash) VALUES (%s, %s)", 
            (user.email, user.password_hash)
        )
        self.connection.commit()
        return {"message": "User registered successfully"}