from user_account_management.models import User, PasswordResetToken
from user_account_management.extensions import db
from datetime import datetime

class UserRepository:
    def get_user_by_email(self, email: str) -> User:
        return User.query.filter_by(email=email).first()

    def create_user(self, email: str, password: str, first_name: str, last_name: str) -> User:
        new_user = User(email=email, password=password, first_name=first_name, last_name=last_name)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update_user(self, user: User) -> None:
        db.session.commit()
    
    def create_password_reset_token(self, user: User, token: str, expires_at: datetime) -> PasswordResetToken:
        password_reset_token = PasswordResetToken(user_id=user.id, token=token, expires_at=expires_at)
        db.session.add(password_reset_token)
        db.session.commit()
        return password_reset_token

    def get_password_reset_token_by_token(self, token: str) -> PasswordResetToken:
        return PasswordResetToken.query.filter_by(token=token).first()

    def delete_password_reset_token(self, password_reset_token: PasswordResetToken) -> None:
        db.session.delete(password_reset_token)
        db.session.commit()