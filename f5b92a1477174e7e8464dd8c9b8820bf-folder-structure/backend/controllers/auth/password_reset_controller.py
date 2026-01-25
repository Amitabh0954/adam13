from flask import Blueprint, request, jsonify
from backend.services.auth.password_reset_service import PasswordResetService
import logging

logger = logging.getLogger(__name__)
password_reset_bp = Blueprint('password_reset', __name__)

password_reset_service = PasswordResetService()

@password_reset_bp.route('/password-reset/request', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')

    if not email:
        logger.warning("Email is required for password reset request")
        return jsonify({"message": "Email is required"}), 400

    try:
        password_reset_service.create_password_reset_request(email)
        logger.info(f"Password reset request created for email: {email}")
        return jsonify({"message": "Password reset request created"}), 200
    except ValueError as e:
        logger.warning(f"Password reset request failed: {str(e)}")
        return jsonify({"message": str(e)}), 400

@password_reset_bp.route('/password-reset/reset', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        logger.warning("Token and new password are required for password reset")
        return jsonify({"message": "Token and new password are required"}), 400

    try:
        password_reset_service.reset_password(token, new_password)
        logger.info("Password reset successful")
        return jsonify({"message": "Password reset successful"}), 200
    except ValueError as e:
        logger.warning(f"Password reset failed: {str(e)}")
        return jsonify({"message": str(e)}), 400