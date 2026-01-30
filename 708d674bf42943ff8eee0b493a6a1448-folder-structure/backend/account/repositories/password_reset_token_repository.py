# Epic Title: Password Recovery

from account.models.password_reset_token import PasswordResetToken
from django.contrib.auth.models import User
from typing import Optional

class PasswordResetTokenRepository:

    def create_token(self, user: User) -> PasswordResetToken:
        token = PasswordResetToken(user=user)
        token.save()
        return token

    def get_token(self, token: str) -> Optional[PasswordResetToken]:
        try:
            return PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            return None

    def delete_token(self, token: PasswordResetToken) -> None:
        token.delete()