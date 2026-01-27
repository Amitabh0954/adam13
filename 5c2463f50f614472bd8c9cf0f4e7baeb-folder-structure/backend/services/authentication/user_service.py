from backend.repositories.authentication.user_repository import UserRepository
from backend.models.user import User
from backend.extensions import bcrypt
import time

class UserService:
    FAILED_LOGIN_LIMIT = 5
    FAILED_LOGIN_TIME_FRAME = 3600  # 1 hour in seconds

    def __init__(self):
        self.user_repository = UserRepository()
        self.failed_login_attempts = {}
    
    def register_user(self, email: str, password: str):
        if not self.is_email_unique(email):
            raise ValueError("Email is already registered.")
        
        if not self.is_password_secure(password):
            raise ValueError("Password does not meet security criteria.")
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed_password)
        self.user_repository.save_user(new_user)
    
    def authenticate_user(self, email: str, password: str) -> User:
        if self.is_login_attempts_exceeded(email):
            raise ValueError("Too many invalid login attempts. Please try again later.")
        
        user = self.user_repository.find_by_email(email)
        if user and bcrypt.check_password_hash(user.password, password):
            self.clear_failed_attempts(email)
            return user
        else:
            self.record_failed_attempt(email)
            return None
    
    def is_email_unique(self, email: str) -> bool:
        return self.user_repository.find_by_email(email) is None
    
    def is_password_secure(self, password: str) -> bool:
        return len(password) >= 8
    
    def record_failed_attempt(self, email: str):
        current_time = time.time()
        if email not in self.failed_login_attempts:
            self.failed_login_attempts[email] = []
        self.failed_login_attempts[email].append(current_time)
    
    def is_login_attempts_exceeded(self, email: str) -> bool:
        current_time = time.time()
        if email in self.failed_login_attempts:
            self.failed_login_attempts[email] = [attempt for attempt in self.failed_login_attempts[email] if current_time - attempt < self.FAILED_LOGIN_TIME_FRAME]
            return len(self.failed_login_attempts[email]) >= self.FAILED_LOGIN_LIMIT
        return False
    
    def clear_failed_attempts(self, email: str):
        if email in self.failed_login_attempts:
            del self.failed_login_attempts[email]