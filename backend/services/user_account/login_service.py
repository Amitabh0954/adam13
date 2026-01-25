from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
from sqlalchemy.sql import func
from backend.repositories.user_account.user_repository import UserRepository
from backend.repositories.user_account.models.user import User

class LoginService:
    LOGIN_ATTEMPT_LIMIT = 5
    LOCK_TIME_MINUTES = 15

    def __init__(self, session: Session):
        self.user_repository = UserRepository(session)
        self.session = session

    def login_user(self, email: str, password: str) -> User:
        user = self.user_repository.get_user_by_email(email)
        
        if not user:
            raise ValueError("Invalid email or password")

        if not user.is_active or (user.login_attempts >= self.LOGIN_ATTEMPT_LIMIT and func.now() - user.last_login_attempt < self.LOCK_TIME_MINUTES * 60):
            raise ValueError("Account is locked due to too many invalid login attempts, try again later")

        if not check_password_hash(user.password, password):
            self.user_repository.increment_login_attempts(user)
            raise ValueError("Invalid email or password")

        self.user_repository.reset_login_attempts(user)
        return user

#### 4. Implement a controller to expose the API for user login

##### LoginController