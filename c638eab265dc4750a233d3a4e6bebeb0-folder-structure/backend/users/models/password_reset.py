# Epic Title: Password Recovery

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def is_expired(self) -> bool:
        return timezone.now() > self.created_at + timedelta(hours=24)

    def __str__(self) -> str:
        return f"Password reset token for {self.user.username}"