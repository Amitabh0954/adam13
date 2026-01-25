from backend.repositories.user_account_management.user_repository import UserRepository
import re

class UserRegistrationService:

    def __init__(self):
        self.user_repository = UserRepository()
        self.email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.password_criteria = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        
    def register(self, email: str, password: str):
        if not re.match(self.email_regex, email):
            raise ValueError("Invalid email format")
        if not re.match(self.password_criteria, password):
            raise ValueError("Password does not meet security criteria")
        
        existing_user = self.user_repository.get_user_by_email(email)
        if existing_user:
            raise ValueError("Email already in use")
        
        return self.user_repository.create_user(email, password)