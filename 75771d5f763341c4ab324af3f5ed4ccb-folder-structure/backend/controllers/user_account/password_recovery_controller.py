# Epic Title: Password Recovery

from flask import Blueprint, request, jsonify
from services.user_account.password_recovery_service import PasswordRecoveryService
from validators.user_account.password_recovery_validator import PasswordRecoveryValidator

password_recovery_controller = Blueprint('password_recovery_controller', __name__)

@password_recovery_controller.route('/recover-password', methods=['POST'])
def recover_password():
    data = request.get_json()
    validator = PasswordRecoveryValidator(data)
    if validator.is_valid():
        service = PasswordRecoveryService()
        response = service.initiate_recovery(data)
        return jsonify(response), 200
    return jsonify(validator.errors), 400

@password_recovery_controller.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    validator = PasswordRecoveryValidator(data, is_reset=True)
    if validator.is_valid():
        service = PasswordRecoveryService()
        response = service.reset_password(data)
        return jsonify(response), 200
    return jsonify(validator.errors), 400