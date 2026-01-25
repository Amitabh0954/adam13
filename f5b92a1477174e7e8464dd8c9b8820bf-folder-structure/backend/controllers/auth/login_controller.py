from flask import Blueprint, request, jsonify
from flask_login import login_user
from backend.services.auth.login_service import LoginService
import logging

logger = logging.getLogger(__name__)
login_bp = Blueprint('login', __name__)

login_service = LoginService()

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        logger.warning("Email and password are required")
        return jsonify({"message": "Email and password are required"}), 400

    try:
        user = login_service.authenticate(email, password)
        if user:
            login_user(user)
            logger.info(f"User '{email}' logged in successfully")
            return jsonify({"message": "Login successful"}), 200
        else:
            logger.warning("Invalid credentials")
            return jsonify({"message": "Invalid credentials"}), 401
    except ValueError as e:
        logger.warning(f"Login failed: {str(e)}")
        return jsonify({"message": str(e)}), 400