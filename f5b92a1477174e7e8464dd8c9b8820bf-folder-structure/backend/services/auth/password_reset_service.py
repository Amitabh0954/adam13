from backend.repositories.user_account_management.password_reset_repository import PasswordResetRepository
from backend.repositories.user_account_management.user_repository import UserRepository
import smtplib

class PasswordResetService:
    
    def __init__(self):
        self.reset_repository = PasswordResetRepository()
        self.user_repository = UserRepository()
    
    def send_reset_email(self, email: str):
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("Email not found")
        
        reset_token = self.reset_repository.create_reset_token(email)
        
        # Simulate sending an email
        smtp = smtplib.SMTP('smtp.example.com')
        smtp.sendmail('noreply@example.com', email, f"Reset your password using this token: {reset_token.token}")
        
    def reset_password(self, token: str, new_password: str):
        reset = self.reset_repository.validate_reset_token(token)
        self.reset_repository.update_password(reset.user_id, new_password)