from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
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
        logger.warning("Email and password are required for login")
        return jsonify({"message": "Email and password are required"}), 400

    user = login_service.authenticate_user(email, password)
    if user:
        login_user(user)
        logger.info(f"User logged in with email: {email}")
        return jsonify({"message": "Login successful"}), 200
    else:
        logger.warning(f"Login failed for email: {email}")
        return jsonify({"message": "Invalid credentials"}), 401

@login_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    logger.info("User logged out")
    return jsonify({"message": "Logout successful"}), 200