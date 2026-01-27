from backend.repositories.authentication.user_repository import UserRepository
from backend.models.user import User
from backend.extensions import bcrypt, db
from backend.utils import send_email
from itsdangerous import URLSafeTimedSerializer

class UserService:
    TOKEN_EXPIRATION = 86400  # 24 hours in seconds

    def __init__(self):
        self.user_repository = UserRepository()
        self.serializer = URLSafeTimedSerializer('a_secret_key')  # you should use a secure key

    def register_user(self, email: str, password: str):
        if not self.is_email_unique(email):
            raise ValueError("Email is already registered.")
        
        if not self.is_password_secure(password):
            raise ValueError("Password does not meet security criteria.")
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(email=email, password=hashed_password)
        self.user_repository.save_user(new_user)
    
    def authenticate_user(self, email: str, password: str) -> User:
        user = self.user_repository.find_by_email(email)
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None
    
    def generate_password_reset_token(self, email: str) -> str:
        user = self.user_repository.find_by_email(email)
        if not user:
            raise ValueError("Email not found.")
        return self.serializer.dumps(user.id)
    
    def send_password_reset_email(self, email: str, reset_link: str):
        subject = "Password Reset Request"
        body = f"Please use the following link to reset your password: {reset_link}"
        send_email(subject, email, body)
    
    def reset_password(self, token: str, new_password: str):
        try:
            user_id = self.serializer.loads(token, max_age=self.TOKEN_EXPIRATION)
            user = self.user_repository.find_by_id(user_id)
            if not user:
                raise ValueError("Invalid token.")
            
            if not self.is_password_secure(new_password):
                raise ValueError("Password does not meet security criteria.")

            user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            self.user_repository.save_user(user)
        except Exception:
            raise ValueError("Invalid or expired token.")
    
    def is_email_unique(self, email: str) -> bool:
        return self.user_repository.find_by_email(email) is None
    
    def is_password_secure(self, password: str) -> bool:
        return len(password) >= 8