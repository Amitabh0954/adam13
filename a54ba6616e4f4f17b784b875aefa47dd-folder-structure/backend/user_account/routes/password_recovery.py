# Epic Title: User Account Management
from flask import Blueprint, request, jsonify
from services.password_recovery_service import PasswordRecoveryService

password_recovery_bp = Blueprint('password_recovery', __name__)
password_recovery_service = PasswordRecoveryService()

@password_recovery_bp.route('/request_reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    email = data.get('email')
    
    response = password_recovery_service.request_password_reset(email)
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200

@password_recovery_bp.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')
    
    response = password_recovery_service.reset_password(token, new_password)
    if response.get("error"):
        return jsonify(response), 400
    
    return jsonify(response), 200