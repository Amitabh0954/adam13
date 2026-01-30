# Epic Title: Password Recovery

from account.repositories.password_reset_token_repository import PasswordResetTokenRepository
from account.repositories.user_repository import UserRepository
from django.core.mail import send_mail
from django.conf import settings
from typing import Optional

class PasswordResetService:
    def __init__(self):
        self.token_repository = PasswordResetTokenRepository()
        self.user_repository = UserRepository()

    def request_password_reset(self, email: str) -> Optional[str]:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return None
        
        token = self.token_repository.create_token(user)
        reset_link = f"{settings.FRONTEND_URL}/reset-password/{token.token}/"

        # Send email (This assumes email backend is properly configured in settings)
        send_mail(
            'Password Reset Request',
            f'Click the link to reset your password: {reset_link}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return reset_link

    def reset_password(self, token_str: str, new_password: str) -> bool:
        token = self.token_repository.get_token(token_str)
        if not token or not token.is_valid():
            return False
        
        user = token.user
        user.set_password(new_password)
        user.save()

        self.token_repository.delete_token(token)
        return True