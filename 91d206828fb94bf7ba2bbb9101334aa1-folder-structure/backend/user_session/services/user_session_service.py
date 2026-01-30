# Epic Title: User Account Management
from repositories.user_session_repository import UserSessionRepository
from werkzeug.security import check_password_hash

class UserSessionService:
    def __init__(self):
        self.user_session_repository = UserSessionRepository()

    def authenticate_user(self, email: str, password: str) -> dict:
        user = self.user_session_repository.get_user_by_email(email)
        
        if user and check_password_hash(user["password"], password):
            return user
        return {}