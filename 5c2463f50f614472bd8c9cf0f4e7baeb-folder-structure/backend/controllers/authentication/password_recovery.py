# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.authentication.password_recovery_service import PasswordRecoveryService

password_recovery_bp = Blueprint('password_recovery', __name__)
password_recovery_service = PasswordRecoveryService()

@password_recovery_bp.route('/request-password-reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    response = password_recovery_service.initiate_password_reset(email)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@password_recovery_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        return jsonify({"error": "Token and new password are required"}), 400

    response = password_recovery_service.reset_password(token, new_password)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200