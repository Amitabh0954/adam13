# Epic Title: User Account Management
from repositories.user_management.password_reset_repository import PasswordResetRepository
from repositories.user_management.user_repository import UserRepository
from datetime import datetime, timedelta
import bcrypt
import uuid

class PasswordRecoveryService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.password_reset_repository = PasswordResetRepository()

    def initiate_password_reset(self, email: str) -> dict:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return {"error": "User not found"}

        token = str(uuid.uuid4())
        expires_at = datetime.utcnow() + timedelta(hours=24)
        self.password_reset_repository.create_reset_token(user['id'], token, expires_at)

        # In a real implementation, send an email with the token here
        # send_password_reset_email(email, token)
        
        return {"message": "Password reset link sent to email"}

    def reset_password(self, token: str, new_password: str) -> dict:
        reset_entry = self.password_reset_repository.get_reset_entry_by_token(token)
        if not reset_entry or reset_entry['expires_at'] < datetime.utcnow():
            return {"error": "Invalid or expired token"}
        
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.user_repository.update_password(reset_entry['user_id'], hashed_password)
        self.password_reset_repository.delete_reset_entry(token)
        
        return {"message": "Password has been reset"}