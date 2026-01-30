# Epic Title: User Account Management
from flask import Blueprint, request, jsonify, session
from services.profile_management_service import ProfileManagementService

profile_management_bp = Blueprint('profile_management', __name__)
profile_service = ProfileManagementService()

@profile_management_bp.route('/update_profile', methods=['PUT'])
def update_profile():
    if 'user_id' not in session:
        return jsonify({"error": "User must be logged in to update profile"}), 401

    user_id = session['user_id']
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    preferences = data.get('preferences', {})

    response = profile_service.update_profile(user_id, name, email, preferences)
    if response.get("error"):
        return jsonify(response), 400

    return jsonify(response), 200