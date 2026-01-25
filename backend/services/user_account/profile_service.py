from sqlalchemy.orm import Session
from backend.repositories.user_account.user_repository import UserRepository
from backend.repositories.user_account.models.user import User
from marshmallow import ValidationError
from .schemas.profile_update_schema import ProfileUpdateSchema

class ProfileService:
    def __init__(self, session: Session):
        self.user_repository = UserRepository(session)

    def update_profile(self, user_id: int, data: dict) -> User:
        user = self.user_repository.get_user_by_email(user_id)
        if not user:
            raise ValueError("User not found")

        try:
            valid_data = ProfileUpdateSchema().load(data, partial=True)
        except ValidationError as err:
            raise ValueError(f"Invalid data: {err.messages}")

        for key, value in valid_data.items():
            setattr(user, key, value)

        self.user_repository.update_user(user)
        return user

##### Profile Update Schema