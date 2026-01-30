# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.password_recovery_service import PasswordRecoveryService

password_recovery_bp = Blueprint('password_recovery', __name__)
password_recovery_service = PasswordRecoveryService()

@password_recovery_bp.route('/recover-password', methods=['POST'])
def recover_password():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    response = password_recovery_service.send_recovery_email(email)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200

@password_recovery_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    data = request.get_json()
    new_password = data.get('new_password')

    if not new_password:
        return jsonify({"error": "New password is required"}), 400

    response = password_recovery_service.reset_password(token, new_password)

    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200