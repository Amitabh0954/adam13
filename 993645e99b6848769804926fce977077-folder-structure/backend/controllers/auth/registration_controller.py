from flask import Blueprint, request, jsonify
from backend.services.auth.registration_service import RegistrationService
import logging

logger = logging.getLogger(__name__)
registration_bp = Blueprint('registration', __name__)

registration_service = RegistrationService()

@registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        logger.warning("Email and password are required for registration")
        return jsonify({"message": "Email and password are required"}), 400

    try:
        registration_service.register_user(email, password)
        logger.info(f"User registered with email: {email}")
        return jsonify({"message": "Registration successful"}), 201
    except ValueError as e:
        logger.warning(f"Registration failed: {str(e)}")
        return jsonify({"message": str(e)}), 400