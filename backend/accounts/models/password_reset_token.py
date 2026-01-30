# Epic Title: Password Recovery

from django.db import models
from backend.accounts.models.user import User
from datetime import datetime, timedelta

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    EXPIRY_TIME = timedelta(hours=24)

    def is_valid(self) -> bool:
        return datetime.now() - self.created_at < self.EXPIRY_TIME
    
    def __str__(self) -> str:
        return f"Password reset token for {self.user.email}"