# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.password_recovery_service import PasswordRecoveryService

password_recovery_bp = Blueprint('password_recovery', __name__)

@password_recovery_bp.route('/password-reset/request', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    recovery_service = PasswordRecoveryService()
    response = recovery_service.request_password_reset(data['email'])
    return jsonify(response), 200

@password_recovery_bp.route('/password-reset/confirm', methods=['POST'])
def confirm_password_reset():
    data = request.get_json()
    recovery_service = PasswordRecoveryService()
    response = recovery_service.confirm_password_reset(data['token'], data['new_password'])
    return jsonify(response), 200