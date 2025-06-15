#!/usr/bin/python3


from flask import Flask, request, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'your_super_secret_key'
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    },
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

@auth.error_handler
def basic_auth_error():
    return make_response(jsonify({"error": "Unauthorized"}), 401)

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={
        "username": username,
        "role": user["role"]
    })
    return jsonify(access_token=token), 200

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200

@jwt.unauthorized_loader
def handle_unauthorized_error(msg):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(msg):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(header, payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(header, payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_fresh_token_error(header, payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()
