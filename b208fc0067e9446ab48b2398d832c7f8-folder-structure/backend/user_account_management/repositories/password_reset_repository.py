# Epic Title: Password Recovery

from user_account_management.models.password_reset_token import PasswordResetToken
from user_account_management.models.user import User
from typing import Optional
import uuid

class PasswordResetRepository:

    def create_token(self, user: User) -> PasswordResetToken:
        token = uuid.uuid4().hex
        reset_token = PasswordResetToken(user=user, token=token)
        reset_token.save()
        return reset_token

    def get_token(self, token: str) -> Optional[PasswordResetToken]:
        try:
            return PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            return None