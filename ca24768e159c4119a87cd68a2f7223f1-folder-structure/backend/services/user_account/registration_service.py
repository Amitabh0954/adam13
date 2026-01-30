# Epic Title: User Account Management
import re
import mysql.connector

class RegistrationService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_db"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def validate_email(self, email: str) -> bool:
        # Check if email is valid
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def validate_password(self, password: str) -> bool:
        # Password must be at least 8 characters long, contain upper and lower case letters, numbers, and special characters
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$'
        return re.match(password_regex, password) is not None

    def is_email_unique(self, email: str) -> bool:
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone() is None

    def register_user(self, email: str, password: str) -> dict:
        if not self.validate_email(email):
            return {"error": "Invalid email format"}

        if not self.validate_password(password):
            return {"error": "Password must be at least 8 characters long and contain upper and lower case letters, numbers, and special characters"}

        if not self.is_email_unique(email):
            return {"error": "Email already exists"}

        query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        self.cursor.execute(query, (email, password))
        self.connection.commit()
        return {"message": "User registered successfully"}

        self.connection.close()