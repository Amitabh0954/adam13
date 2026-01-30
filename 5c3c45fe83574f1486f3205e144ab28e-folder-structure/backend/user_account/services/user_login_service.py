# Epic Title: User Account Management
from repositories.user_repository import UserRepository
from werkzeug.security import check_password_hash
import logging

class UserLoginService:
    MAX_LOGIN_ATTEMPTS = 5

    def __init__(self):
        self.user_repository = UserRepository()
        self.login_attempts = {}

    def login_user(self, data: dict) -> dict:
        email = data.get('email')
        password = data.get('password')

        if email in self.login_attempts and self.login_attempts[email] >= self.MAX_LOGIN_ATTEMPTS:
            return {"error": "Account locked due to too many failed login attempts"}

        user = self.user_repository.get_user_by_email(email)
        if user and check_password_hash(user['password'], password):
            self.login_attempts[email] = 0  # Reset login attempts on successful login
            logging.info(f"User {email} successfully logged in.")
            return {"user_id": user['id']}
        
        self.login_attempts[email] = self.login_attempts.get(email, 0) + 1
        logging.warning(f"Failed login attempt for user {email}. Attempt {self.login_attempts[email]}.")
        return {"error": "Invalid email or password"}