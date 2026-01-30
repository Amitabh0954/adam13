# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from backend.services.user_account.password_reset_service import PasswordResetService

password_reset_bp = Blueprint('password_reset', __name__)
password_reset_service = PasswordResetService()

@password_reset_bp.route('/api/user_account/request_password_reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"error": "Email is required"}), 400

    response = password_reset_service.send_reset_link(email)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200

@password_reset_bp.route('/api/user_account/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')

    if not token or not new_password:
        return jsonify({"error": "Token and new password are required"}), 400

    response = password_reset_service.reset_password(token, new_password)
    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 200