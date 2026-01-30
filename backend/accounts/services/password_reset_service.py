# Epic Title: Password Recovery

from backend.accounts.repositories.user_repository import UserRepository
from backend.accounts.repositories.password_reset_token_repository import PasswordResetTokenRepository
from backend.accounts.models.user import User
from backend.accounts.models.password_reset_token import PasswordResetToken
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

class PasswordResetService:
    def __init__(self, user_repository: UserRepository, token_repository: PasswordResetTokenRepository) -> None:
        self.user_repository = user_repository
        self.token_repository = token_repository

    def send_reset_email(self, email: str) -> None:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("No user found with this email")
        
        token = self.token_repository.create_token(user)
        reset_link = f"https://example.com/reset_password?token={token.token}"
        
        send_mail(
            "Password Reset Request",
            f"Click the link to reset your password: {reset_link}",
            "no-reply@example.com",
            [email],
            fail_silently=False,
        )
        logger.info(f"Password reset email sent to {email}")

    def reset_password(self, token: str, new_password: str) -> None:
        password_reset_token = self.token_repository.get_token(token)
        if not password_reset_token or not password_reset_token.is_valid():
            raise ValueError("Invalid or expired password reset token")

        user = password_reset_token.user
        user.password = new_password
        user.save()
        self.token_repository.invalidate_token(password_reset_token)
        logger.info(f"Password reset successful for {user.email}")