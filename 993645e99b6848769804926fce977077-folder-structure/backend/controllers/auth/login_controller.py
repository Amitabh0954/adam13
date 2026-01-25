from flask import Blueprint, request, jsonify, session
from backend.services.auth.login_service import LoginService
import logging

logger = logging.getLogger(__name__)
auth_bp = Blueprint('auth', __name__)

login_service = LoginService()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        logger.warning("Email and password are required")
        return jsonify({"message": "Email and password are required"}), 400

    try:
        user = login_service.authenticate(email, password)
        session['user_id'] = user.id
        logger.info(f"User logged in with email: {email}")
        return jsonify({"message": "Login successful"}), 200
    except ValueError as e:
        logger.warning(f"Login failed: {str(e)}")
        return jsonify({"message": str(e)}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    logger.info("User logged out")
    return jsonify({"message": "Logout successful"}), 200