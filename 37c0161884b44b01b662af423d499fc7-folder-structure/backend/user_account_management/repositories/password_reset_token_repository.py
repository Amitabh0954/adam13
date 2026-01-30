# Epic Title: Password Recovery

from typing import Optional
from user_account_management.models.password_reset_token import PasswordResetToken
from user_account_management.models.user import User

class PasswordResetTokenRepository:

    def create_reset_token(self, user: User, token: str) -> PasswordResetToken:
        reset_token = PasswordResetToken(user=user, token=token)
        reset_token.save()
        return reset_token

    def get_active_token(self, token: str) -> Optional[PasswordResetToken]:
        try:
            reset_token = PasswordResetToken.objects.get(token=token, is_active=True)
            if reset_token.is_valid():
                return reset_token
            reset_token.is_active = False
            reset_token.save()
            return None
        except PasswordResetToken.DoesNotExist:
            return None

    def deactivate_token(self, token: str) -> None:
        reset_token = self.get_active_token(token)
        if reset_token:
            reset_token.is_active = False
            reset_token.save()