from user_account_management.models import User
from user_account_management.extensions import db

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