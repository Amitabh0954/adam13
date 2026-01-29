# Epic Title: User Account Management

from flask import Flask, request, jsonify
import mysql.connector
from backend.repositories.user_account.user_repository import UserRepository
from backend.services.user_account.user_service import UserService

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydatabase"
    )

    user_repository = UserRepository(db_connection)
    user_service = UserService(user_repository)
    result = user_service.register_user(email, password)

    if result:
        return jsonify({'error': result}), 400

    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)