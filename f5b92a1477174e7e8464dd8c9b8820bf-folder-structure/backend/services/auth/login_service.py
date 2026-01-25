from backend.repositories.user_account_management.user_repository import UserRepository

class LoginService:

    def __init__(self):
        self.user_repository = UserRepository()
    
    def authenticate(self, email: str, password: str):
        user = self.user_repository.get_user_by_email(email)
        if user and self.user_repository.verify_password(user, password):
            return user
        return None