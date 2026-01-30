# Epic Title: Password Recovery

from django.db import models
from django.utils import timezone
from user_account_management.models.user import User

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def is_valid(self) -> bool:
        return self.is_active and (timezone.now() - self.created_at).total_seconds() < 86400  # 24 hours

    def __str__(self) -> str:
        return f'Token for {self.user.email}'