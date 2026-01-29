# Epic Title: Password Recovery

from repositories.user_account.user_repository import UserRepository
from hashlib import sha256
import time
import uuid

class PasswordRecoveryService:
    def __init__(self):
        self.user_repository = UserRepository()

    def initiate_recovery(self, data: dict) -> dict:
        user = self.user_repository.find_user_by_email(data['email'])
        if user:
            token = str(uuid.uuid4())
            expiry_time = int(time.time()) + 24 * 3600
            self.user_repository.save_recovery_token(user['id'], token, expiry_time)
            return {"msg": "Recovery email sent"}
        return {"error": "User not found"}
    
    def reset_password(self, data: dict) -> dict:
        user = self.user_repository.find_user_by_token(data['token'])
        if user and user['token_expiry_time'] > int(time.time()):
            hashed_password = sha256(data['new_password'].encode('utf-8')).hexdigest()
            self.user_repository.update_password(user['id'], hashed_password)
            return {"msg": "Password updated successfully"}
        return {"error": "Invalid or expired token"}