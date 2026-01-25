from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from flask_mail import Mail, Message
from backend.repositories.user_account.user_repository import UserRepository
from backend.repositories.user_account.models.user import User
from werkzeug.security import generate_password_hash
import secrets

class PasswordResetService:
    TOKEN_EXPIRY_HOURS = 24

    def __init__(self, session: Session, mail: Mail):
        self.user_repository = UserRepository(session)
        self.mail = mail

    def generate_reset_token(self, email: str):
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("Email not found")

        token = secrets.token_urlsafe()
        expires_at = datetime.utcnow() + timedelta(hours=self.TOKEN_EXPIRY_HOURS)
        self.user_repository.set_reset_token(user, token, expires_at)

        msg = Message("Password Reset Request", recipients=[email])
        msg.body = f"Your password reset link is: http://example.com/reset_password?token={token}"
        self.mail.send(msg)

    def verify_reset_token(self, token: str) -> User:
        user = self.user_repository.get_user_by_reset_token(token)
        if not user or user.reset_token_expires_at < datetime.utcnow():
            raise ValueError("Invalid or expired token")
        return user

    def reset_password(self, token: str, new_password: str):
        user = self.verify_reset_token(token)
        user.password = generate_password_hash(new_password)
        self.user_repository.clear_reset_token(user)
        self.user_repository.update_user(user)

#### 4. Implement controllers to expose the API for password reset and email verification