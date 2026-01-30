# Epic Title: User Account Management

from datetime import datetime, timedelta
import uuid

class PasswordResetToken:
    def __init__(self, user_id: int, token: str = None, expires_at: datetime = None):
        self.user_id = user_id
        self.token = token or str(uuid.uuid4())
        self.expires_at = expires_at or (datetime.now() + timedelta(hours=24))

    def is_expired(self) -> bool:
        return datetime.now() > self.expires_at