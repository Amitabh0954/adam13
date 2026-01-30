# Epic Title: Password Recovery

from backend.repositories.password_reset_repository import PasswordResetRepository
from backend.repositories.user_repository import UserRepository
from django.core.mail import send_mail
from django.conf import settings
import uuid
from typing import Tuple

class PasswordResetService:
    def __init__(self):
        self.password_reset_repository = PasswordResetRepository()
        self.user_repository = UserRepository()

    def request_password_reset(self, email: str) -> Tuple[bool, str]:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return False, 'User not found'

        self.password_reset_repository.invalidate_reset_requests(user)
        reset_request = self.password_reset_repository.create_reset_request(user)
        
        reset_link = f"{settings.FRONTEND_URL}/reset-password/{reset_request.token}/"
        send_mail(
            'Password Reset Request',
            f'Please use the following link to reset your password: {reset_link}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        
        return True, 'Password reset link has been sent to your email'

    def reset_password(self, token: str, new_password: str) -> Tuple[bool, str]:
        reset_request = self.password_reset_repository.get_reset_request_by_token(token)
        if not reset_request or reset_request.is_expired:
            return False, 'Invalid or expired password reset token'

        user = reset_request.user
        user.set_password(new_password)
        user.save()
        
        reset_request.delete() # invalidate the used token

        return True, 'Password has been reset successfully'