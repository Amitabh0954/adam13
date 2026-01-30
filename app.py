# Epic Title: User Registration

import logging
from backend.accounts.repositories.user_repository import UserRepository
from backend.accounts.services.user_service import UserService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    user_repository = UserRepository()
    user_service = UserService(user_repository=user_repository)

    try:
        user_service.register_user("test@example.com", "SecurePass123")
        logger.info("User registration successful")
    except Exception as e:
        logger.error(f"User registration failed: {e}")

if __name__ == "__main__":
    main()