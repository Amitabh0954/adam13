from flask import Blueprint, request, jsonify
from backend.services.user_account.user_registration_service import UserRegistrationService
import logging

logger = logging.getLogger(__name__)
user_registration_bp = Blueprint('user_registration', __name__)

user_registration_service = UserRegistrationService()

@user_registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        logger.warning("Email and password are required")
        return jsonify({"message": "Email and password are required"}), 400

    try:
        user = user_registration_service.register(email, password)
        logger.info(f"User '{email}' registered successfully")
        return jsonify({"message": "User registered successfully"}), 201
    except ValueError as e:
        logger.warning(f"Failed to register user: {str(e)}")
        return jsonify({"message": str(e)}), 400