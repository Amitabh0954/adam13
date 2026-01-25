from backend.repositories.user_account_management.user_repository import UserRepository
from backend.repositories.user_account_management.password_reset_token_repository import PasswordResetTokenRepository
from backend.models.user import User
from backend.models.password_reset_token import PasswordResetToken
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer
import smtplib
import logging
from email.message import EmailMessage

logger = logging.getLogger(__name__)

class PasswordResetService:
    
    def __init__(self):
        self.user_repository = UserRepository()
        self.password_reset_token_repository = PasswordResetTokenRepository()
        self.serializer = URLSafeTimedSerializer("secret-key")  # Replace "secret-key" with a real secret key

    def send_password_reset_email(self, email: str) -> None:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise ValueError("Email not found")

        token = self.password_reset_token_repository.create_token(user.id)
        reset_link = f"https://your-domain.com/reset-password/{token.token}"
        
        self._send_email(user.email, reset_link)

    def reset_password(self, token: str, new_password: str) -> None:
        token_record = self.password_reset_token_repository.get_token(token)
        if not token_record or token_record.is_expired():
            raise ValueError("Invalid or expired token")

        user = self.user_repository.get_user_by_id(token_record.user_id)
        user.password = generate_password_hash(new_password)
        self.user_repository.save_user(user)
        self.password_reset_token_repository.delete_token(token_record)

    def _send_email(self, recipient_email: str, reset_link: str) -> None:
        sender_email = "no-reply@your-domain.com"
        message = EmailMessage()
        message.set_content(f"Click the link to reset your password: {reset_link}")
        message["Subject"] = "Password Reset Request"
        message["From"] = sender_email
        message["To"] = recipient_email

        with smtplib.SMTP("smtp.your-email-server.com") as server:
            server.login("your-email-username", "your-email-password")
            server.send_message(message)
        logger.info(f"Password reset email sent to {recipient_email}")