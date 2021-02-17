from flask import Blueprint, jsonify, request
from flask_jwt_extended import (create_access_token, 
    get_jwt_claims, jwt_refresh_token_required, 
    create_refresh_token, get_jwt_identity
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS

from server.util.instances import jwt
from server.models.User import User
from server.util.instances import db


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
        return {'status': 'error', 'msg': 'Email not provided'}, 400
    
    if not password:
        return {'status': 'error', 'msg': 'Password not provided'}, 400

    user = User.query.filter_by(email=email).first()

    if user is None:
        return {'status': 'error', 'msg': 'No user with this email, please check details and try again'}, 401

    if check_password_hash(user.password,password) is False:
        return {'status': 'error', 'msg': 'Invalid Password, please check details and try again'}, 401

    access_token = create_access_token(identity=user.json())
    refresh_token = create_refresh_token(identity=user.json())
    return jsonify({'status': 'success', 'token':access_token, 'refreshToken': refresh_token}), 200



@authRoute.route('/create', methods=['POST'])
def create():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    phone = request.json.get('phone', None)
    name = request.json.get('name', None)

    if not email:
        return {'status': 'error', 'msg': 'Email not provided'}, 400
    
    if not password:
        return {'status': 'error', 'msg': 'Password not provided'}, 400

    if not name:
        return {'status': 'error', 'msg': 'Name not provided'}, 400
    
    if not phone:
        return {'status': 'error', 'msg': 'Phone number not provided'}, 400

    user = User.query.filter_by(email=email).first()

    if user is not None:
        return {'status': 'error', 'msg': 'Email address already exist! try login'}, 400

    user = User(
        name=name,
        password=generate_password_hash(password),
        email=email,
        phone=phone,
        username=email.split('@')[0]
    )

    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)

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