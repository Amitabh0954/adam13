# Epic Title: Password Recovery

from users.models.password_reset import PasswordResetToken
from django.contrib.auth.models import User
from typing import Optional
from django.utils.crypto import get_random_string

class PasswordResetRepository:

    def create_password_reset_token(self, user: User) -> PasswordResetToken:
        token = get_random_string(64)
        password_reset_token = PasswordResetToken(user=user, token=token)
        password_reset_token.save()
        return password_reset_token

    def get_password_reset_token(self, token: str) -> Optional[PasswordResetToken]:
        try:
            return PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            return None

    def delete_password_reset_token(self, token: str) -> None:
        PasswordResetToken.objects.filter(token=token).delete()