# Epic Title: User Account Management

from flask import Blueprint, request, jsonify, session
from backend.user_account_management.services.profile_service import ProfileService
import logging

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/update', methods=['POST'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'User must be logged in to update profile'}), 401

    data = request.get_json()
    profile_service = ProfileService()
    result = profile_service.update_profile(user_id, data)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Profile updated successfully'}), 200