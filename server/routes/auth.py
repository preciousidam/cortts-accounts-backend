from flask import Blueprint, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_claims
from werkzeug.security import check_password_hash, generate_password_hash

from server.util.instances import jwt
from server.models.User import User


authRoute = Blueprint('auth', __name__, url_prefix='/api/auth')
CORS(authRoute)

@jwt.user_claims_loader
def add_details_to_token(identity):
    return identity


@authRoute.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return {'status': 'error', 'msg': 'Email not provide'}, 400
    
    if not password:
        return {'status': 'error', 'msg': 'Password not provide'}, 400

    user = User.query.filter_by(email=email).first()

    if user is None:
        return {'status': 'error', 'msg': 'No user with this email, please check details and try again'}, 401

    if check_password_hash(user.password,password) is False:
        return {'status': 'error', 'msg': 'Invalid Password, please check details and try again'}, 401

    access_token = create_access_token(identity=user.json())
    return jsonify({'status': 'success', 'token':access_token}), 200