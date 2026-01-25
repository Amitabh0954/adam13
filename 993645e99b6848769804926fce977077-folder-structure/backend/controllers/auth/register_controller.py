from flask import Blueprint, request, jsonify
from backend.services.auth.user_service import UserService
import logging

logger = logging.getLogger(__name__)
auth_bp = Blueprint('auth', __name__)

user_service = UserService()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        logger.warning("Email and password are required")
        return jsonify({"message": "Email and password are required"}), 400

    try:
        user_service.register_user(email, password)
        logger.info(f"User registered with email: {email}")
        return jsonify({"message": "User registered successfully"}), 201
    except ValueError as e:
        logger.warning(f"Registration failed: {str(e)}")
        return jsonify({"message": str(e)}), 400