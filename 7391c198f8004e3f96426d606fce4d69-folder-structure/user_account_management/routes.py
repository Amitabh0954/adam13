from flask import request, jsonify, session
from flask_login import login_user, logout_user, login_required, LoginManager, current_user
from werkzeug.security import check_password_hash
from . import user_blueprint
from .models import User
from .extensions import db
import datetime

login_manager = LoginManager()
login_manager.login_view = 'user.login'

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password, password):
        session.permanent = True
        login_user(user)
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        record_invalid_login_attempt(email)
        return jsonify({"error": "Invalid email or password"}), 401

@user_blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def record_invalid_login_attempt(email: str):
    # Here you would implement your logic to track the invalid attempts and lock the account if needed.
    pass

@user_blueprint.before_request
def before_request():
    session.modified = True