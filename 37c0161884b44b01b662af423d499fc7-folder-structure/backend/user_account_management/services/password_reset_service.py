# Epic Title: Password Recovery

import uuid
from typing import Optional
from django.core.mail import send_mail
from user_account_management.repositories.user_repository import UserRepository
from user_account_management.repositories.password_reset_token_repository import PasswordResetTokenRepository
from user_account_management.models.user import User

class PasswordResetService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.token_repository = PasswordResetTokenRepository()

    def request_password_reset(self, email: str) -> Optional[str]:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return None
        
        token = str(uuid.uuid4())
        self.token_repository.create_reset_token(user, token)
        self.send_reset_email(user.email, token)
        return token

    def send_reset_email(self, email: str, token: str) -> None:
        reset_link = f'http://example.com/reset-password?token={token}'
        send_mail(
            'Password Reset Request',
            f'Click the link to reset your password: {reset_link}',
            'no-reply@example.com',
            [email],
        )

    def reset_password(self, token: str, new_password: str) -> bool:
        reset_token = self.token_repository.get_active_token(token)
        if not reset_token:
            return False
        
        user = reset_token.user
        user.password = new_password
        user.save()
        self.token_repository.deactivate_token(token)
        return True