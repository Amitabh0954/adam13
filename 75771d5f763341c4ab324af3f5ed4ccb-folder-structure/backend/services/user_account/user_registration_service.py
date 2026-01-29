# Epic Title: User Registration

from repositories.user_account.user_repository import UserRepository
from hashlib import sha256

class UserRegistrationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, data: dict) -> dict:
        password_hash = sha256(data['password'].encode('utf-8')).hexdigest()
        user_data = {
            'email': data['email'],
            'password': password_hash,
            'first_name': data['first_name'],
            'last_name': data['last_name'],
        }
        result = self.user_repository.save_user(user_data)
        return {"msg": "User registered successfully", "user_id": result.inserted_id}