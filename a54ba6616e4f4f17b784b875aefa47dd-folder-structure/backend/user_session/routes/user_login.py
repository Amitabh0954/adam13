# Epic Title: User Account Management
from flask import Blueprint, request, jsonify, session
from services.user_login_service import UserLoginService

user_login_bp = Blueprint('user_login', __name__)
login_service = UserLoginService()

@user_login_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    response = login_service.login_user(email, password)
    if response.get("error"):
        return jsonify(response), 401
    
    session['user_id'] = response.get('user_id')
    session.permanent = True
    return jsonify(response), 200