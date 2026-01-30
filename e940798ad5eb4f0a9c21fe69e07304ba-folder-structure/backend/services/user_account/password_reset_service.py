# Epic Title: User Account Management
from backend.models.user_account.user import User
from backend.repositories.user_account_repository import UserAccountRepository
from backend.models.user_account.password_reset_token import PasswordResetToken
from werkzeug.security import generate_password_hash
import smtplib
from email.mime.text import MIMEText

class PasswordResetService:
    RESET_URL = "http://localhost:5000/api/user_account/reset_password?token="

    def __init__(self):
        self.user_account_repository = UserAccountRepository()

    def send_reset_link(self, email: str) -> dict:
        user_data = self.user_account_repository.find_user_by_email(email)
        if not user_data:
            return {"error": "User not found"}

        reset_token = self.user_account_repository.create_password_reset_token(user_data['id'])
        reset_link = f"{self.RESET_URL}{reset_token.token}"

        self._send_email(email, reset_link)
        return {"message": "Password reset link sent to email"}

    def _send_email(self, to_email: str, reset_link: str):
        msg = MIMEText(f"Click the link to reset your password: {reset_link}")
        msg['Subject'] = 'Password Reset'
        msg['From'] = 'no-reply@example.com'
        msg['To'] = to_email

        with smtplib.SMTP('localhost') as server:
            server.sendmail(msg['From'], [msg['To']], msg.as_string())

    def reset_password(self, token: str, new_password: str) -> dict:
        token_data = self.user_account_repository.get_password_reset_token(token)
        if not token_data:
            return {"error": "Invalid or expired token"}

        reset_token = PasswordResetToken(
            user_id=token_data['user_id'], 
            token=token_data['token'], 
            expires_at=token_data['expires_at']
        )
        if reset_token.is_expired():
            self.user_account_repository.invalidate_password_reset_token(token)
            return {"error": "Invalid or expired token"}

        if not User.validate_password(new_password):
            return {"error": "Password does not meet security criteria"}

        password_hash = generate_password_hash(new_password)
        self.user_account_repository.update_user_password(reset_token.user_id, password_hash)
        self.user_account_repository.invalidate_password_reset_token(token)
        return {"message": "Password has been reset successfully"}