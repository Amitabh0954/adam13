from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime
from backend.repositories.user_account_management.user_repository import UserRepository
from backend.repositories.user_account_management.password_reset_repository import PasswordResetRepository
from backend.models.user import User
import smtplib

class PasswordResetService:
    
    def __init__(self):
        self.user_repository = UserRepository()
        self.password_reset_repository = PasswordResetRepository()
        self.serializer = URLSafeTimedSerializer('SECRET_KEY')

    def create_password_reset_request(self, email: str) -> None:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("Email not found")

        token = self.serializer.dumps(email, salt='password-reset-salt')
        self.password_reset_repository.create_password_reset(user.id, token)
        self.send_password_reset_email(user.email, token)

    def send_password_reset_email(self, email: str, token: str) -> None:
        reset_url = f"http://localhost:5000/password-reset/reset?token={token}"
        subject = "Password Reset Requested"
        body = f"Please click the link to reset your password: {reset_url}"
        
        # Example of sending email - replace with actual SMTP configuration
        sender = "noreply@example.com"
        password = "examplepassword"

        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, email, f"Subject: {subject}\n\n{body}")

    def reset_password(self, token: str, new_password: str) -> None:
        password_reset = self.password_reset_repository.get_password_reset_by_token(token)
        if not password_reset:
            raise ValueError("Invalid token")

        if password_reset.expires_at < datetime.utcnow():
            self.password_reset_repository.delete_password_reset(password_reset)
            raise ValueError("Token has expired")

        user = self.user_repository.get_user_by_id(password_reset.user_id)
        if not user:
            raise ValueError("User not found")

        user.password = generate_password_hash(new_password)
        self.user_repository.save_user(user)
        self.password_reset_repository.delete_password_reset(password_reset)