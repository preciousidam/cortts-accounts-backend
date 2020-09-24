from flask import Blueprint, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import jwt_required

from server.models.Clients import Tenant
from server.util.instances import db


tenantsRoute = Blueprint('tenants', __name__,url_prefix='/api/tenants')

@tenantsRoute.route('/', methods=['GET'])
def get_all_tenants():
    tenants = Tenant.query.all()
    return jsonify({'data': tenants, 'msg': 'success'}), 200


@tenantsRoute.route('/<path:path>', methods=['GET'])
def get_account(path):
    tenants = Tenant.query.filter_by(id=path).first()
    return jsonify({'data': tenants, 'msg': 'success'}), 200


@tenantsRoute.route('/create', methods=['POST'])
@jwt_required
def create_tenants():

    if request.method == 'POST':
        name = request.json.get('name')
        email = request.json.get('email')
        address = request.json.get('address')
        contactPerson = request.json.get('contactPerson')
        phone = request.json.get('phone')

    if not name:
        return jsonify({'msg': 'Missing Tenant Name', 'status': 'failed'}), 400

    if not email:
        return jsonify({'msg': 'Missing Tenant Email', 'status': 'failed'}), 400

    if not address:
        return jsonify({'msg': 'Missing Tenant Address', 'status': 'failed'}), 400

    if not phone:
        return jsonify({'msg': 'Missing Tenant Phone', 'status': 'failed'}), 400

    if not contactPerson:
        return jsonify({'msg': 'Missing Tenant Contact Person', 'status': 'failed'}), 400

    tenant = Tenant(
        name=name,
        email=email,
        address=address,
        phone=phone,
        contactPerson=contactPerson,
    )

    db.session.add(tenant)
    db.session.commit()


    tenants = Tenant.query.all()
    return jsonify({'data': tenants, 'msg': 'Tenant saved', 'status': 'success'}), 201


@tenantsRoute.route('/delete', methods=['POST'])
@jwt_required
def delete_tenants():
   
    if request.method == 'POST':
        id = request.json.get('id')
    

    if not id:
        return jsonify({'msg': 'Missing Tenant ID', 'status': 'failed'}), 400

    

    Tenant.query.filter_by(id=id).delete()

    db.session.commit()


    tenants = Tenant.query.all()
    return jsonify({'data': tenants, 'msg': 'Tenant deleted', 'status': 'success'}), 201

