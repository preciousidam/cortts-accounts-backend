from flask import Blueprint, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import jwt_required

from server.models.Clients import Landlord
from server.util.instances import db


landlordsRoute = Blueprint('landlords', __name__,url_prefix='/api/landlords')

@landlordsRoute.route('/', methods=['GET'])
def get_all_landlords():
    landlords = Landlord.query.all()
    return jsonify({'data': landlords, 'msg': 'success'}), 200


@landlordsRoute.route('/<path:path>', methods=['GET'])
def get_account(path):
    landlords = Landlord.query.filter_by(id=path).first()
    return jsonify({'data': landlords, 'msg': 'success'}), 200


@landlordsRoute.route('/create', methods=['POST'])
@jwt_required
def create_landlords():

    if request.method == 'POST':
        name = request.json.get('name')
        email = request.json.get('email')
        address = request.json.get('address')
        contactPerson = request.json.get('contactPerson')
        phone = request.json.get('phone')

    if not name:
        return jsonify({'msg': 'Missing Landlord Name', 'status': 'failed'}), 400

    if not email:
        return jsonify({'msg': 'Missing Landlord Email', 'status': 'failed'}), 400

    if not address:
        return jsonify({'msg': 'Missing Landlord Address', 'status': 'failed'}), 400

    if not phone:
        return jsonify({'msg': 'Missing Landlord Phone', 'status': 'failed'}), 400

    if not contactPerson:
        return jsonify({'msg': 'Missing Landlord Contact Person', 'status': 'failed'}), 400

    landlord = Landlord(
        name=name,
        email=email,
        address=address,
        phone=phone,
        contactPerson=contactPerson,
    )

    db.session.add(landlord)
    db.session.commit()


    landlords = Landlord.query.all()
    return jsonify({'data': landlords, 'msg': 'Landlord saved', 'status': 'success'}), 201


@landlordsRoute.route('/delete', methods=['POST'])
@jwt_required
def delete_landlords():
   
    if request.method == 'POST':
        id = request.json.get('id')
    

    if not id:
        return jsonify({'msg': 'Missing Landlord ID', 'status': 'failed'}), 400

    

    Landlord.query.filter_by(id=id).delete()

    db.session.commit()


    landlords = Landlord.query.all()
    return jsonify({'data': landlords, 'msg': 'Landlord deleted', 'status': 'success'}), 201

