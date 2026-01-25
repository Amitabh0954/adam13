import uuid
import smtplib
from datetime import datetime, timedelta
from backend.repositories.auth.password_reset_repository import PasswordResetRepository
from backend.repositories.auth.user_repository import UserRepository

class PasswordResetService:
    TOKEN_EXPIRATION = 24  # hours

    def __init__(self):
        self.password_reset_repository = PasswordResetRepository()
        self.user_repository = UserRepository()

    def send_password_reset_link(self, email: str) -> None:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("User with this email does not exist")

        token = self.password_reset_repository.create_password_reset_token(user)
        self._send_email(user.email, token.token)

    def reset_password(self, token: str, new_password: str) -> None:
        user = self.password_reset_repository.get_user_by_reset_token(token)
        user.password = new_password
        self.password_reset_repository.delete_password_reset_token(token)
        self.user_repository.save_user(user)

    def _send_email(self, email: str, token: str) -> None:
        reset_url = f"http://example.com/reset-password?token={token}"
        message = f"Click the link to reset your password: {reset_url}"
        with smtplib.SMTP('smtp.example.com') as server:
            server.sendmail('noreply@example.com', email, message)