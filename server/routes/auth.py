from flask import Blueprint, jsonify, request
from flask_jwt_extended import (create_access_token, 
    get_jwt_claims, jwt_refresh_token_required, 
    create_refresh_token, get_jwt_identity
)
from werkzeug.security import check_password_hash, generate_password_hash

from server.util.instances import jwt
from server.models.User import User


authRoute = Blueprint('auth', __name__, url_prefix='/api/auth')

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
    refresh_token = create_refresh_token(identity=user.json())
    return jsonify({'status': 'success', 'token':access_token, 'refreshToken': refresh_token}), 200


@authRoute.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'token': create_access_token(identity=current_user)
    }
    return jsonify(ret), 200