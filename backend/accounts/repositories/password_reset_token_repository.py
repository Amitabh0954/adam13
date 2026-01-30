# Epic Title: Password Recovery

from backend.accounts.models.password_reset_token import PasswordResetToken
from backend.accounts.models.user import User
from django.utils.crypto import get_random_string

class PasswordResetTokenRepository:
    def create_token(self, user: User) -> PasswordResetToken:
        token = get_random_string(50)
        password_reset_token = PasswordResetToken(user=user, token=token)
        password_reset_token.save()
        return password_reset_token

    def get_token(self, token: str) -> PasswordResetToken:
        return PasswordResetToken.objects.filter(token=token).first()

    def invalidate_token(self, token: PasswordResetToken) -> None:
        token.delete()