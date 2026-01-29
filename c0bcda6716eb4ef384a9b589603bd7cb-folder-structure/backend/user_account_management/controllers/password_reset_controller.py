# Epic Title: User Account Management

from flask import Blueprint, request, jsonify
from structured_logging import get_logger
from backend.user_account_management.services.password_reset_service import PasswordResetService
from backend.user_account_management.repositories.user_repository import UserRepository
from backend.user_account_management.repositories.password_reset_repository import PasswordResetRepository

password_reset_blueprint = Blueprint('password_reset_controller', __name__)
logger = get_logger(__name__)

@password_reset_blueprint.route('/reset_password_request', methods=['POST'])
def reset_password_request():
    data = request.json
    email = data.get('email')
    
    user_repository = UserRepository()  # Ideally should be injected
    password_reset_repository = PasswordResetRepository()  # Ideally should be injected
    password_reset_service = PasswordResetService(user_repository, password_reset_repository)
    
    token = password_reset_service.create_reset_request(email)
    if token is None:
        return jsonify({'message': 'Password reset request failed'}), 400
    
    return jsonify({'message': 'Password reset request successful', 'token': token})

@password_reset_blueprint.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.json
    token = data.get('token')
    new_password = data.get('password')
    
    user_repository = UserRepository()  # Ideally should be injected
    password_reset_repository = PasswordResetRepository()  # Ideally should be injected
    password_reset_service = PasswordResetService(user_repository, password_reset_repository)
    
    success = password_reset_service.reset_password(token, new_password)
    if not success:
        return jsonify({'message': 'Password reset failed'}), 400
    
    return jsonify({'message': 'Password reset successful'})