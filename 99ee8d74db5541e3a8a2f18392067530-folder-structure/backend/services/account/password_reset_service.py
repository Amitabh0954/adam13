# Epic Title: User Account Management

from backend.repositories.user_repository.password_reset_repository import PasswordResetRepository
from backend.repositories.user_repository.user_repository import UserRepository
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime, timedelta
from typing import Dict

class PasswordResetService:
    def __init__(self):
        self.password_reset_repository = PasswordResetRepository()
        self.user_repository = UserRepository()
        self.serializer = URLSafeTimedSerializer('secret-signing-key')  # Use a secure key in production

    def initiate_password_reset(self, email: str) -> Dict[str, str]:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return {'status': 'error', 'message': 'Email not found'}

        token = self.serializer.dumps(email, salt='password-reset-salt')
        self.password_reset_repository.create_reset_token(user.id, token)
        # Here send the token to the user's email. (Omitted for simplicity)
        return {'status': 'success', 'message': 'Password reset link sent'}

    def reset_password(self, token: str, new_password: str) -> Dict[str, str]:
        try:
            email = self.serializer.loads(token, salt='password-reset-salt', max_age=86400)  # token valid for 24 hrs
        except:
            return {'status': 'error', 'message': 'Invalid or expired token'}

        user = self.user_repository.get_user_by_email(email)
        if not user:
            return {'status': 'error', 'message': 'User not found'}

        self.user_repository.update_user_password(user.id, new_password)
        self.password_reset_repository.delete_reset_token(token)  # Invalidate the token
        return {'status': 'success', 'message': 'Password updated successfully'}