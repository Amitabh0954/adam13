from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from backend.services.user_management.profile_service import ProfileService

profile_blueprint = Blueprint('profile', __name__)
profile_service = ProfileService()

@profile_blueprint.route('/profile', methods=['GET'])
@login_required
def get_profile():
    profile = profile_service.get_profile(current_user.id)
    return jsonify(profile), 200

@profile_blueprint.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    profile = profile_service.update_profile(current_user.id, data)
    return jsonify(profile), 200