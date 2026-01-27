# Epic Title: User Account Management

from flask import Blueprint, request, jsonify, session
from backend.services.account.user_service import UserService

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user_service = UserService()
    result = user_service.register_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'User registered successfully'}), 201

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user_service = UserService()
    result = user_service.login_user(email, password)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    session['user_id'] = result['user_id']
    return jsonify({'message': 'User logged in successfully'}), 200