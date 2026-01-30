# Epic Title: Password Recovery

from accounts.authentication.repositories.password_reset_repository import PasswordResetRepository
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.conf import settings

class PasswordResetService:
    def __init__(self):
        self.reset_repository = PasswordResetRepository()

    def request_password_reset(self, email: str) -> bool:
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return False

        token = get_random_string(64)
        self.reset_repository.create_reset_token(user, token)

        reset_link = f"{settings.FRONTEND_URL}/reset-password/{token}"
        send_mail(
            'Password Reset Request',
            f'Please use the following link to reset your password: {reset_link}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return True

    def reset_password(self, token: str, new_password: str) -> bool:
        user = self.reset_repository.get_user_by_token(token)
        if not user:
            return False

        user.set_password(new_password)
        user.save()
        self.reset_repository.delete_reset_token(token)
        return True