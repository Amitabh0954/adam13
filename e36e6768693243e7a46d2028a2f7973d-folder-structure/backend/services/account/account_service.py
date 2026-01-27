# Epic Title: User Account Management

from backend.repositories.account.account_repository import AccountRepository
from backend.models.user import User
import re
import hashlib
import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from typing import Dict

class AccountService:
    def __init__(self):
        self.account_repository = AccountRepository()

    def register_user(self, email: str, password: str) -> Dict[str, str]:
        if self.account_repository.get_user_by_email(email):
            return {'status': 'error', 'message': 'Email must be unique'}

        if not self.is_password_secure(password):
            return {'status': 'error', 'message': 'Password does not meet security criteria'}

        hashed_password = generate_password_hash(password)
        self.account_repository.create_user(email, hashed_password)
        return {'status': 'success', 'message': 'User registered successfully'}

    def login_user(self, email: str, password: str) -> Dict[str, str]:
        user = self.account_repository.get_user_by_email(email)
        if not user or not check_password_hash(user.password, password):
            return {'status': 'error', 'message': 'Invalid email or password'}

        return {'status': 'success', 'message': 'User logged in successfully', 'user_id': user.id}

    def is_password_secure(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True

    def initiate_password_reset(self, email: str) -> Dict[str, str]:
        user = self.account_repository.get_user_by_email(email)
        if not user:
            return {'status': 'error', 'message': 'Email not found'}

        # Generate a unique token
        token = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
        
        # Set expiry time as 24 hours from now
        expiry_time = datetime.utcnow() + timedelta(hours=24)

        # Save the token and expiry time
        self.account_repository.save_password_reset_token(user.id, token, expiry_time)

        # Send email with the token
        self.send_password_reset_email(email, token)

        return {'status': 'success', 'message': 'Password reset link sent'}

    def reset_password(self, token: str, new_password: str) -> Dict[str, str]:
        reset_request = self.account_repository.get_password_reset_request(token)
        if not reset_request or reset_request.expiry_time < datetime.utcnow():
            return {'status': 'error', 'message': 'Invalid or expired token'}

        if not self.is_password_secure(new_password):
            return {'status': 'error', 'message': 'Password does not meet security criteria'}

        hashed_password = generate_password_hash(new_password)
        self.account_repository.update_user_password(reset_request.user_id, hashed_password)
        self.account_repository.delete_password_reset_request(token)

        return {'status': 'success', 'message': 'Password reset successfully'}

    def send_password_reset_email(self, email: str, token: str):
        msg = MIMEText(f"Click the link to reset your password: http://yourapp.com/reset_password?token={token}")
        msg['Subject'] = 'Password Reset Request'
        msg['From'] = 'no-reply@yourapp.com'
        msg['To'] = email

        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)