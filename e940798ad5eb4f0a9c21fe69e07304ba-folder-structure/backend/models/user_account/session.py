# Epic Title: User Account Management

from datetime import datetime, timedelta

class Session:
    def __init__(self, user_id: int, session_token: str, expires_at: datetime):
        self.user_id = user_id
        self.session_token = session_token
        self.expires_at = expires_at

    def is_expired(self) -> bool:
        return datetime.now() > self.expires_at

    def extend(self, duration: timedelta):
        self.expires_at = datetime.now() + duration