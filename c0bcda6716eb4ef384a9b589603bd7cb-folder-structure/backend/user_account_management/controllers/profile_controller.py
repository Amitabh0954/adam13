# Epic Title: User Account Management

from flask import Blueprint, request, jsonify
from structured_logging import get_logger
from backend.user_account_management.services.profile_service import ProfileService
from backend.user_account_management.repositories.profile_repository import ProfileRepository

profile_blueprint = Blueprint('profile_controller', __name__)
logger = get_logger(__name__)

@profile_blueprint.route('/profile', methods=['GET'])
def get_profile():
    user_id = request.args.get('user_id')
    
    profile_repository = ProfileRepository()  # Ideally should be injected
    profile_service = ProfileService(profile_repository)
    
    profile = profile_service.get_profile(user_id)
    if profile is None:
        return jsonify({'message': 'Profile not found'}), 404
    
    return jsonify({
        'user_id': profile.user_id,
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'preferences': profile.preferences
    })

@profile_blueprint.route('/profile', methods=['PUT'])
def update_profile():
    data = request.json
    user_id = data.get('user_id')
    first_name = data.get('first_name', "")
    last_name = data.get('last_name', "")
    preferences = data.get('preferences', "")
    
    profile_repository = ProfileRepository()  # Ideally should be injected
    profile_service = ProfileService(profile_repository)
    
    profile = profile_service.update_profile(user_id, first_name, last_name, preferences)
    if profile is None:
        return jsonify({'message': 'Profile update failed'}), 400
    
    return jsonify({'message': 'Profile updated successfully'})