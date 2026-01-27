from datetime import datetime, timedelta

class InvalidLoginAttemptTracker:
    def __init__(self):
        self.attempts = {}

    def add_attempt(self, user_id: int):
        now = datetime.now()
        if user_id in self.attempts:
            self.attempts[user_id].append(now)
        else:
            self.attempts[user_id] = [now]

    def is_locked_out(self, user_id: int, max_attempts: int, lockout_period: timedelta) -> bool:
        if user_id not in self.attempts:
            return False

        attempts = [attempt for attempt in self.attempts[user_id] if datetime.now() - attempt < lockout_period]
        self.attempts[user_id] = attempts

        return len(attempts) >= max_attempts

tracker = InvalidLoginAttemptTracker()

def setup_database():
    db.create_all()