from sqlalchemy.orm import Session
from .models.user import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        return user

    def get_user_by_email(self, email: str) -> User:
        return self.session.query(User).filter_by(email=email).first()

#### 3. Implement services for user registration ensuring email uniqueness and password security criteria

##### RegistrationService