# Epic Title: User Account Management

from flask import Blueprint, request, jsonify
from structured_logging import get_logger
from backend.user_account_management.services.login_service import LoginService
from backend.user_account_management.repositories.user_repository import UserRepository
from backend.user_account_management.repositories.session_repository import SessionRepository

login_blueprint = Blueprint('login_controller', __name__)
logger = get_logger(__name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    user_repository = UserRepository()  # Ideally should be injected
    session_repository = SessionRepository()  # Ideally should be injected
    login_service = LoginService(user_repository, session_repository)
    
    session = login_service.login(email, password)
    if session is None:
        return jsonify({'message': 'Invalid credentials or user already logged in'}), 400
    
    return jsonify({'message': 'Login successful', 'session_id': session.id})

@login_blueprint.route('/logout', methods=['POST'])
def logout():
    data = request.json
    session_id = data.get('session_id')
    
    session_repository = SessionRepository()  # Ideally should be injected
    login_service = LoginService(None, session_repository)  # UserRepository not needed for logout
    
    login_service.logout(session_id)
    return jsonify({'message': 'Logout successful'})