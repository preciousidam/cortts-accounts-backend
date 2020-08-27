from flask import Blueprint, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import jwt_required

from server.models.Account import Account
from server.util.instances import db


accountsRoute = Blueprint('accounts', __name__,url_prefix='/api/accounts')

@accountsRoute.route('/', methods=['GET'])
def get_all_accounts():
    accounts = Account.query.all()
    return jsonify({'data': accounts, 'msg': 'success'}), 200


@accountsRoute.route('/<path:path>', methods=['GET'])
def get_account(path):
    accounts = Account.query.filter_by(id=path).first()
    return jsonify({'data': accounts, 'msg': 'success'}), 200


@accountsRoute.route('/create', methods=['POST'])
@jwt_required
def create_accounts():
    number = None
    name = None
    sort_code = None
    bank = None
    balance = None

    if request.method == 'POST':
        number = request.json.get('number')
        name = request.json.get('name')
        sort_code = request.json.get('sc')
        balance = request.json.get('balance')
        bank = request.json.get('bank')

    if not number:
        return jsonify({'msg': 'Missing Acct Number', 'status': 'failed'}), 400

    if not name:
        return jsonify({'msg': 'Missing Acct Name', 'status': 'failed'}), 400

    if not balance:
        return jsonify({'msg': 'Missing Acct Balance', 'status': 'failed'}), 400

    if not bank:
        return jsonify({'msg': 'Missing Acct Bank', 'status': 'failed'}), 400

    if not sort_code:
        return jsonify({'msg': 'Missing Acct Sort Code', 'status': 'failed'}), 400

    acct = Account(
        number=number,
        name=name,
        balance=balance,
        sort_code=sort_code,
        bank=bank,
    )

    db.session.add(acct)
    db.session.commit()


    accounts = Account.query.all()
    return jsonify({'data': accounts, 'msg': 'Account saved', 'status': 'success'}), 201


@accountsRoute.route('/delete', methods=['POST'])
@jwt_required
def delete_accounts():
    id = None
    

    if request.method == 'POST':
        id = request.json.get('id')
    

    if not id:
        return jsonify({'msg': 'Missing Acct ID', 'status': 'failed'}), 400

    

    Account.query.filter_by(id=id).delete()

    db.session.commit()


    accounts = Account.query.all()
    return jsonify({'data': accounts, 'msg': 'Account deleted', 'status': 'success'}), 201

