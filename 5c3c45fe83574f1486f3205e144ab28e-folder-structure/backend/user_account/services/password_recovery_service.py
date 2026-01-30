# Epic Title: User Account Management
import uuid
import hashlib
import logging
from datetime import datetime, timedelta
from repositories.user_repository import UserRepository
from repositories.password_reset_repository import PasswordResetRepository
from werkzeug.security import generate_password_hash

class PasswordRecoveryService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.password_reset_repository = PasswordResetRepository()

    def request_password_reset(self, email: str) -> dict:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            return {"error": "User not found"}

        token = self._generate_token(email)
        self.password_reset_repository.create_password_reset_request(user['id'], token)

        # Here, normally you would send an email with the reset link containing the token
        logging.info(f"Password reset link sent to {email}")
        return {"message": "Password reset link has been sent to your email"}

    def confirm_password_reset(self, token: str, new_password: str) -> dict:
        reset_request = self.password_reset_repository.get_password_reset_request(token)
        if not reset_request:
            return {"error": "Invalid or expired token"}

        if reset_request['expires_at'] < datetime.now():
            return {"error": "Token has expired"}

        hashed_password = generate_password_hash(new_password)
        self.user_repository.update_user_password(reset_request['user_id'], hashed_password)
        self.password_reset_repository.delete_password_reset_request(token)
        
        logging.info(f"Password for user {reset_request['user_id']} has been reset successfully")
        return {"message": "Password has been reset successfully"}

    def _generate_token(self, email: str) -> str:
        return hashlib.sha256((email + str(uuid.uuid4())).encode()).hexdigest()