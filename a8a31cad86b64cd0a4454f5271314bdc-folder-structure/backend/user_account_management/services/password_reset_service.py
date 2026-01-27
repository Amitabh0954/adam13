# Epic Title: User Account Management

import jwt
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from backend.user_account_management.repositories.password_reset_repository import PasswordResetRepository
from backend.user_account_management.repositories.user_repository import UserRepository
from typing import Dict
from flask import current_app

class PasswordResetService:
    def __init__(self):
        self.password_reset_repository = PasswordResetRepository()
        self.user_repository = UserRepository()

    def initiate_password_reset(self, email: str) -> Dict[str, str]:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return {'status': 'error', 'message': 'Email not found'}

        token = self.generate_reset_token(email)
        self.password_reset_repository.save_password_reset_token(user.id, token)
        
        # Send email logic here (skipped for brevity)

        return {'status': 'success', 'message': 'Password reset token generated'}

    def reset_password(self, token: str, new_password: str) -> Dict[str, str]:
        user_id = self.verify_reset_token(token)
        if not user_id:
            return {'status': 'error', 'message': 'Invalid or expired token'}

        hashed_password = generate_password_hash(new_password, method='sha256')
        self.user_repository.update_user_password(user_id, hashed_password)
        self.password_reset_repository.invalidate_password_reset_token(user_id)

        return {'status': 'success', 'message': 'Password reset successfully'}

    def generate_reset_token(self, email: str) -> str:
        expires = datetime.utcnow() + timedelta(hours=24)
        payload = {'email': email, 'exp': expires}
        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
        return token

    def verify_reset_token(self, token: str) -> int:
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            email = payload['email']
            user = self.user_repository.get_user_by_email(email)
            if user:
                return user.id
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        return None