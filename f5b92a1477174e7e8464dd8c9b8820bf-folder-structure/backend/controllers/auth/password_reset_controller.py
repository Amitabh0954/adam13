from flask import Blueprint, request, jsonify
from backend.services.auth.password_reset_service import PasswordResetService
import logging

logger = logging.getLogger(__name__)
password_reset_bp = Blueprint('password_reset', __name__)

password_reset_service = PasswordResetService()

@password_reset_bp.route('/request-password-reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')

    if not email:
        logger.warning("Email is required to request password reset")
        return jsonify({"message": "Email is required"}), 400

    try:
        password_reset_service.send_password_reset_email(email)
        logger.info(f"Password reset email sent to {email}")
        return jsonify({"message": "Password reset email sent"}), 200
    except ValueError as e:
        logger.warning(f"Password reset request failed: {str(e)}")
        return jsonify({"message": str(e)}), 400

@password_reset_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        logger.warning("Token and new password are required to reset password")
        return jsonify({"message": "Token and new password are required"}), 400

    try:
        password_reset_service.reset_password(token, new_password)
        logger.info("Password reset successfully")
        return jsonify({"message": "Password reset successfully"}), 200
    except ValueError as e:
        logger.warning(f"Password reset failed: {str(e)}")
        return jsonify({"message": str(e)}), 400