# Epic Title: Password Recovery

from user_account_management.repositories.password_reset_repository import PasswordResetRepository
from user_account_management.repositories.user_repository import UserRepository
from user_account_management.models.user import User
from user_account_management.models.password_reset_token import PasswordResetToken
from typing import Optional
from django.core.mail import send_mail

class PasswordResetService:
    def __init__(self):
        self.password_reset_repository = PasswordResetRepository()
        self.user_repository = UserRepository()

    def request_password_reset(self, email: str) -> Optional[PasswordResetToken]:
        user = self.user_repository.get_user_by_email(email)
        if user:
            reset_token = self.password_reset_repository.create_token(user)
            self.send_reset_email(user, reset_token.token)
            return reset_token
        return None

    def validate_token(self, token: str) -> bool:
        reset_token = self.password_reset_repository.get_token(token)
        if reset_token and not reset_token.is_expired():
            return True
        return False

    def reset_password(self, token: str, new_password: str) -> bool:
        token_record = self.password_reset_repository.get_token(token)
        if token_record and not token_record.is_expired():
            user = token_record.user
            user.set_password(new_password)
            user.save()
            token_record.delete()
            return True
        return False

    def send_reset_email(self, user: User, token: str) -> None:
        send_mail(
            'Password Reset',
            f'Please use the following link to reset your password: https://example.com/reset-password/{token}',
            'no-reply@example.com',
            [user.email],
            fail_silently=False,
        )