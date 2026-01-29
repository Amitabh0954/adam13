# Epic Title: User Account Management

from typing import Optional, Dict
from backend.repositories.user_account.user_repository import UserRepository
import bcrypt
import secrets
import smtplib
from email.message import EmailMessage

class UserService:
    MAX_FAILED_ATTEMPTS = 5  # configurable
    FAILED_ATTEMPT_INTERVAL_MINUTES = 15  # configurable

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def validate_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isalpha() for char in password):
            return False
        return True

    def register_user(self, email: str, password: str) -> Optional[str]:
        if not self.validate_password(password):
            return "Password must be at least 8 characters long and include both letters and numbers."
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        if self.user_repository.find_user_by_email(email):
            return "Email already registered"

        self.user_repository.create_user(email, hashed_password.decode('utf-8'))
        return None

    def authenticate_user(self, email: str, password: str) -> Optional[str]:
        failed_attempts = self.user_repository.count_recent_failed_attempts(email, self.FAILED_ATTEMPT_INTERVAL_MINUTES)
        if failed_attempts >= self.MAX_FAILED_ATTEMPTS:
            return "Too many failed login attempts. Please try again later."
        
        user = self.user_repository.find_user_by_email(email)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            # Placeholder for session creation logic
            return None
        else:
            self.user_repository.register_failed_attempt(email)
            return "Invalid email or password"
    
    def send_password_reset_email(self, email: str) -> Optional[str]:
        user = self.user_repository.find_user_by_email(email)
        if not user:
            return "No account associated with this email address."
        
        token = secrets.token_urlsafe(16)  # Generates a 24 character base64 token
        self.user_repository.create_password_reset_token(email, token)

        msg = EmailMessage()
        msg.set_content(f"Use the following link to reset your password: http://yourdomain.com/reset-password?token={token}&email={email}")
        msg['Subject'] = 'Password Reset Request'
        msg['From'] = 'noreply@yourdomain.com'
        msg['To'] = email

        try:
            with smtplib.SMTP('localhost') as server:
                server.send_message(msg)
        except Exception as e:
            return f"Cannot send email: {str(e)}"

        return None

    def reset_password(self, email: str, token: str, new_password: str) -> Optional[str]:
        if not self.validate_password(new_password):
            return "Password must be at least 8 characters long and include both letters and numbers."
        
        token_record = self.user_repository.find_password_reset_token(email, token)
        if not token_record:
            return "Invalid or expired password reset token."
        
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        self.user_repository.update_password(email, hashed_password.decode('utf-8'))
        
        return None

    def update_user_profile(self, email: str, profile_data: Dict[str, str]) -> Optional[str]:
        user = self.user_repository.find_user_by_email(email)
        if not user:
            return "User not found."
        
        self.user_repository.update_user_profile(email, profile_data)
        return None