# Epic Title: User Login

from repositories.user_account.user_repository import UserRepository
from hashlib import sha256
import time

class UserLoginService:
    def __init__(self):
        self.user_repository = UserRepository()

    def login_user(self, data: dict) -> dict:
        hashed_password = sha256(data['password'].encode('utf-8')).hexdigest()
        user = self.user_repository.find_user_by_email(data['email'])
        
        if user and user['password'] == hashed_password:
            session = self.create_session(user['id'])
            return {"msg": "Login successful", "session_id": session["id"]}
        return None
    
    def create_session(self, user_id: int) -> dict:
        session_id = self.user_repository.create_session(user_id)
        return {"id": session_id, "user_id": user_id, "start_time": time.time()}