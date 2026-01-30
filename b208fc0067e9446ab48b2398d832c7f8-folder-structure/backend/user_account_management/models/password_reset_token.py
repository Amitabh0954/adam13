# Epic Title: Password Recovery

from django.db import models
from django.utils import timezone
from datetime import timedelta
from user_account_management.models.user import User

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self) -> bool:
        return self.created_at < timezone.now() - timedelta(days=1)

    def __str__(self) -> str:
        return f"PasswordResetToken(user={self.user.email}, token={self.token})"