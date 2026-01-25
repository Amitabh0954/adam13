from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash
from backend.repositories.user_account.user_repository import UserRepository
from backend.repositories.user_account.models.user import User
from marshmallow import ValidationError
from .schemas.user_registration_schema import UserRegistrationSchema

class RegistrationService:
    def __init__(self, session: Session):
        self.user_repository = UserRepository(session)

    def register_user(self, data: dict) -> User:
        try:
            valid_data = UserRegistrationSchema().load(data)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        if self.user_repository.get_user_by_email(valid_data['email']):
            raise ValueError("Email already exists")

        hashed_password = generate_password_hash(valid_data['password'])
        user = User(
            email=valid_data['email'],
            password=hashed_password,
            first_name=valid_data.get('first_name'),
            last_name=valid_data.get('last_name')
        )
        
        return self.user_repository.add_user(user)

##### User Registration Schema