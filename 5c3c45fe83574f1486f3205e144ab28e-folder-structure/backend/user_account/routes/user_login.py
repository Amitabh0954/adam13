# Epic Title: User Account Management
from flask import Blueprint, request, jsonify, session
from services.user_login_service import UserLoginService

user_login_bp = Blueprint('user_login', __name__)

@user_login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_service = UserLoginService()
    response = user_service.login_user(data)
    if response.get("error"):
        return jsonify(response), 401
    session['user_id'] = response['user_id']
    return jsonify(response), 200