# Epic Title: User Account Management

from flask import Blueprint, request, jsonify
from structured_logging import get_logger
from backend.user_account_management.services.user_service import UserService

user_blueprint = Blueprint('user_controller', __name__)
logger = get_logger(__name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    user_service = UserService()  # UserService should ideally be injected
    
    user = user_service.register_user(email, password)
    if user is None:
        return jsonify({'message': 'Registration failed'}), 400
    
    return jsonify({'message': 'User registered successfully', 'user_id': user.id})