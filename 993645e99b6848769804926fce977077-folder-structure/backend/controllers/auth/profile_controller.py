from flask import Blueprint, request, jsonify, session
from backend.services.auth.profile_service import ProfileService
import logging

logger = logging.getLogger(__name__)
auth_bp = Blueprint('auth', __name__)

profile_service = ProfileService()

@auth_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = session.get('user_id')
    if not user_id:
        logger.warning("Unauthorized access attempt to get profile")
        return jsonify({"message": "Unauthorized"}), 401

    user_profile = profile_service.get_user_profile(user_id)
    return jsonify(user_profile), 200

@auth_bp.route('/profile', methods=['PUT'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        logger.warning("Unauthorized access attempt to update profile")
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    profile_service.update_user_profile(user_id, data)
    logger.info(f"User profile updated for user_id: {user_id}")
    return jsonify({"message": "Profile updated successfully"}), 200