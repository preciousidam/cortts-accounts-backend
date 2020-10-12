from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from server.models.OtherModels import Category, Staff
from server.util.instances import db

otherRoute = Blueprint('otherroutes', __name__,url_prefix='/api/routes')

@otherRoute.route('/categories/', methods=['GET'])
def get_all_categories():
    categories = Category.query.all()
    return jsonify({'data': categories, 'msg': 'success'}), 200

@otherRoute.route('/categories/<path:path>', methods=['GET'])
def get_category(path):
    categories = Category.query.filter_by(id=path).first()
    return jsonify({'data': categories, 'msg': 'success'}), 200

@otherRoute.route('/staff/', methods=['GET'])
def get_all_staff():
    staff = Staff.query.all()
    return jsonify({'data': staff, 'msg': 'success'}), 200


@otherRoute.route('/staff/<path:path>', methods=['GET'])
def get_staff(path):
    staff = Staff.query.filter_by(id=path).first()
    return jsonify({'data': staff, 'msg': 'success'}), 200



@otherRoute.route('/categories/create', methods=['POST'])
@jwt_required
def create_category():
    
    if request.method == 'POST':
        title = request.json.get('title')
        

    if not title:
        return jsonify({'msg': 'Missing category title', 'status': 'failed'}), 400


    cat = Category(
        title = title,
    )

    db.session.add(cat)
    db.session.commit()
    db.session.refresh(cat)

    return jsonify({'data': cat, 'msg': 'category added', 'status': 'success'}), 201



@otherRoute.route('/staff/create', methods=['POST'])
@jwt_required
def create_staff():
    
    if request.method == 'POST':
        name = request.json.get('name')
        

    if not name:
        return jsonify({'msg': 'Missing staff name', 'status': 'failed'}), 400


    staff = Staff(
        name = name,
    )

    db.session.add(staff)
    db.session.commit()
    db.session.refresh(staff)

    return jsonify({'data': staff, 'msg': 'staff add', 'status': 'success'}), 201