# Epic Title: Password Recovery

from accounts.authentication.models.password_reset import PasswordResetToken
from django.contrib.auth.models import User
from typing import Optional

class PasswordResetRepository:

    def create_reset_token(self, user: User, token: str) -> PasswordResetToken:
        PasswordResetToken.objects.filter(user=user).delete()
        return PasswordResetToken.objects.create(user=user, token=token)

    def get_user_by_token(self, token: str) -> Optional[User]:
        try:
            reset_token = PasswordResetToken.objects.get(token=token)
            if reset_token.is_expired():
                reset_token.delete()
                return None
            return reset_token.user
        except PasswordResetToken.DoesNotExist:
            return None

    def delete_reset_token(self, token: str):
        PasswordResetToken.objects.filter(token=token).delete()