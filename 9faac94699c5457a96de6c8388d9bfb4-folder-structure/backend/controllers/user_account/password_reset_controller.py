# Epic Title: User Account Management

from flask import Blueprint, request, jsonify
from backend.services.user_account.password_reset_service import PasswordResetService

password_reset_bp = Blueprint('password_reset_bp', __name__)

@password_reset_bp.route('/password-reset/request', methods=['POST'])
def request_password_reset():
    email = request.json.get('email')
    if not email:
        return jsonify({'message': 'Email is required'}), 400

    password_reset_service = PasswordResetService()
    password_reset_service.request_password_reset(email)

    return jsonify({'message': 'Password reset link sent'}), 200

@password_reset_bp.route('/password-reset/confirm', methods=['POST'])
def confirm_password_reset():
    token = request.json.get('token')
    new_password = request.json.get('new_password')

    if not token or not new_password:
        return jsonify({'message': 'Token and new password are required'}), 400

    password_reset_service = PasswordResetService()
    result = password_reset_service.reset_password(token, new_password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Password has been reset'}), 200