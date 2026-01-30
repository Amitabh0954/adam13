# Epic Title: User Login

from django.db import models
from backend.accounts.models.user import User
from datetime import datetime, timedelta

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)

    INACTIVITY_TIMEOUT = timedelta(minutes=30)

    def is_active(self) -> bool:
        return datetime.now() - self.last_activity < self.INACTIVITY_TIMEOUT
    
    def __str__(self) -> str:
        return f"Session for {self.user.email}"