# Epic Title: User Account Management

import logging
from flask import Blueprint, request, jsonify, url_for
from backend.user_account_management.services.password_reset_service import PasswordResetService

password_reset_bp = Blueprint('password_reset_bp', __name__)

@password_reset_bp.route('/request_password_reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'message': 'Email is required'}), 400

    password_reset_service = PasswordResetService()
    result = password_reset_service.initiate_password_reset(email)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Password reset link sent if email exists'}), 200

@password_reset_bp.route('/reset_password/<token>', methods=['POST'])
def reset_password(token: str):
    data = request.get_json()
    new_password = data.get('password')

    if not new_password:
        return jsonify({'message': 'New password is required'}), 400

    password_reset_service = PasswordResetService()
    result = password_reset_service.reset_password(token, new_password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Password reset successful'}), 200