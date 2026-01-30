# Epic Title: User Registration

from backend.accounts.models.user import User

class UserRepository:
    def get_user_by_email(self, email: str) -> User:
        return User.objects.filter(email=email).first()

    def create_user(self, email: str, password: str) -> User:
        user = User(email=email, password=password)
        user.save()
        return user