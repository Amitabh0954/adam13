# Epic Title: User Account Management
from backend.models.user_account.user import User
from backend.repositories.user_account_repository import UserAccountRepository
from datetime import timedelta
from uuid import uuid4

class LoginService:
    MAX_INVALID_ATTEMPTS = 5
    SESSION_DURATION = timedelta(minutes=30)

    def __init__(self):
        self.user_account_repository = UserAccountRepository()

    def login(self, email: str, password: str) -> dict:
        user_data = self.user_account_repository.find_user_by_email(email)
        if not user_data:
            return {"error": "Invalid email or password"}

        user = User(id=user_data['id'], email=user_data['email'], password=user_data['password_hash'])

        if not user.check_password(password):
            invalid_attempts = self.user_account_repository.get_invalid_attempts(user_data['id']) + 1
            self.user_account_repository.update_invalid_attempts(user_data['id'], invalid_attempts)
            if invalid_attempts >= self.MAX_INVALID_ATTEMPTS:
                return {"error": "Account locked due to too many invalid login attempts"}
            return {"error": "Invalid email or password"}
        
        # Reset invalid attempts on successful login
        self.user_account_repository.update_invalid_attempts(user_data['id'], 0)
        
        session_token = str(uuid4())
        self.user_account_repository.register_session(user_data['id'], session_token, self.SESSION_DURATION)
        return {
            "message": "Login successful",
            "session_token": session_token
        }

    def validate_session(self, session_token: str) -> bool:
        session_data = self.user_account_repository.get_session(session_token)
        if not session_data:
            return False

        session = Session(user_id=session_data['user_id'], session_token=session_data['session_token'], expires_at=session_data['expires_at'])
        if session.is_expired():
            self.user_account_repository.invalidate_session(session_token)
            return False
        session.extend(self.SESSION_DURATION)
        self.user_account_repository.register_session(session.user_id, session_token, self.SESSION_DURATION)
        return True