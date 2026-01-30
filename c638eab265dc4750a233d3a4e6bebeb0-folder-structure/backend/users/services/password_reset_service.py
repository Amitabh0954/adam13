# Epic Title: Password Recovery

from users.repositories.password_reset_repository import PasswordResetRepository
from django.contrib.auth.models import User
from users.models.password_reset import PasswordResetToken
from typing import Optional
from django.core.mail import send_mail

class PasswordResetService:
    def __init__(self):
        self.password_reset_repository = PasswordResetRepository()

    def request_password_reset(self, email: str) -> Optional[PasswordResetToken]:
        try:
            user = User.objects.get(email=email)
            password_reset_token = self.password_reset_repository.create_password_reset_token(user)
            self.send_password_reset_email(user, password_reset_token.token)
            return password_reset_token
        except User.DoesNotExist:
            return None

    def reset_password(self, token: str, new_password: str) -> Optional[User]:
        password_reset_token = self.password_reset_repository.get_password_reset_token(token)
        if password_reset_token and not password_reset_token.is_expired():
            user = password_reset_token.user
            user.set_password(new_password)
            user.save()
            self.password_reset_repository.delete_password_reset_token(token)
            return user
        return None

    def send_password_reset_email(self, user: User, token: str) -> None:
        reset_link = f"http://example.com/reset-password?token={token}"
        send_mail(
            'Password Reset Request',
            f'Please use the following link to reset your password: {reset_link}',
            'no-reply@example.com',
            [user.email],
            fail_silently=False,
        )