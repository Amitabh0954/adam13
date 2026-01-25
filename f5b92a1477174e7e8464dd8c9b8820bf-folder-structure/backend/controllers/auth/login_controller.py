from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, current_user
from backend.services.auth.login_service import LoginService
import logging

logger = logging.getLogger(__name__)
login_bp = Blueprint('login', __name__)

login_service = LoginService()

@login_bp.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        logger.info(f"User {current_user.email} is already logged in")
        return jsonify({"message": "Already logged in"}), 200

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        logger.warning("Email and password are required for login")
        return jsonify({"message": "Email and password are required"}), 400

    try:
        user = login_service.authenticate_user(email, password)
        login_user(user)
        logger.info(f"User {user.email} logged in successfully")
        return jsonify({"message": "Login successful"}), 200
    except ValueError as e:
        logger.warning(f"Login failed: {str(e)}")
        return jsonify({"message": str(e)}), 400

@login_bp.route('/logout', methods=['POST'])
def logout():
    if not current_user.is_authenticated:
        return jsonify({"message": "Not logged in"}), 400

    logger.info(f"User {current_user.email} logged out")
    logout_user()
    return jsonify({"message": "Logout successful"}), 200