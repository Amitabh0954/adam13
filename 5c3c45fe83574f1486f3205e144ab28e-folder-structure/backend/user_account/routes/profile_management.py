# Epic Title: User Account Management
from flask import Blueprint, request, jsonify, session
from services.profile_management_service import ProfileManagementService

profile_management_bp = Blueprint('profile_management', __name__)

@profile_management_bp.route('/profile', methods=['GET'])
def get_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    profile_service = ProfileManagementService()
    profile = profile_service.get_profile(user_id)
    return jsonify(profile), 200

@profile_management_bp.route('/profile', methods=['PUT'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    profile_service = ProfileManagementService()
    response = profile_service.update_profile(user_id, data)
    return jsonify(response), 200