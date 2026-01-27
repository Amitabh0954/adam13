# Epic Title: User Account Management

from flask import Blueprint, request, jsonify, session
from backend.services.user_account.profile_service import ProfileService

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unauthorized'}), 401

    profile_service = ProfileService()
    profile = profile_service.get_profile(user_id)

    if profile:
        return jsonify(profile), 200
    return jsonify({'message': 'Profile not found'}), 404

@profile_bp.route('/profile', methods=['PUT'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'message': 'Unauthorized'}), 401

    data = request.get_json()
    profile_service = ProfileService()
    result = profile_service.update_profile(user_id, data)

    if result['status'] == 'error':
        return jsonify({'message': result['message']}), 400

    return jsonify({'message': 'Profile updated successfully'}), 200