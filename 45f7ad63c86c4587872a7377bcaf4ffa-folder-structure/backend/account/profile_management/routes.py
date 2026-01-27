# Epic Title: User Account Management

from flask import Blueprint, request, jsonify, session
from models import User
from database import db_session

profile_management_bp = Blueprint('profile_management_bp', __name__)

@profile_management_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unauthorized access'}), 401
    
    user = User.query.get(user_id)
    if user:
        user_data = {
            'email': user.email,
            'preferences': user.preferences  # Assuming User model has a preferences attribute
        }
        return jsonify(user_data), 200

    return jsonify({'message': 'User not found'}), 404

@profile_management_bp.route('/profile', methods=['PUT'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unauthorized access'}), 401
    
    data = request.get_json()
    user = User.query.get(user_id)
    
    if user:
        user.email = data.get('email', user.email)
        user.preferences = data.get('preferences', user.preferences)  # Assuming User model has a preferences attribute
        db_session.commit()
        return jsonify({'message': 'Profile updated successfully'}), 200

    return jsonify({'message': 'User not found'}), 404