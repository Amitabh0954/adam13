# Epic Title: User Account Management

from flask import Blueprint, request, jsonify, session
from backend.services.user_account.login_service import LoginService

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    login_service = LoginService()
    result = login_service.authenticate_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 401

    session['user_id'] = result['user'].id
    return jsonify({'message': 'Login successful'}), 200

@login_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200