from flask import Blueprint, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import jwt_required

from server.models.Transactions import Transaction
from server.models.Account import Account
from server.util.instances import db

transRoute = Blueprint('transactions', __name__,url_prefix='/api/transactions')



@transRoute.route('/create', methods=['POST'])
def create_transactions():
    acct_id = None
    date = None
    beneficiary = None
    description = None
    amount = None
    transType = None

    if request.method == 'POST':
        acct_id = request.json.get('acct_id')
        date = request.json.get('date')
        beneficiary = request.json.get('beneficiary')
        description = request.json.get('description')
        amount = request.json.get('amount')
        transType = request.json.get('transType')
        print(request.get_json())
        

    if not acct_id:
        return jsonify({'msg': 'Missing Acct Id', 'status': 'failed'}), 400

    if not date:
        return jsonify({'msg': 'Missing Transaction date', 'status': 'failed'}), 400

    if not beneficiary:
        return jsonify({'msg': 'Missing Transaction Beneficiary', 'status': 'failed'}), 400

    if not description:
        return jsonify({'msg': 'Missing Transaction description', 'status': 'failed'}), 400

    if not amount:
        return jsonify({'msg': 'Missing Transaction amount', 'status': 'failed'}), 400

    
    if not transType:
        return jsonify({'msg': 'Missing Transaction transType', 'status': 'failed'}), 400



    tran = Transaction(
        account_id = acct_id,
        date = date,
        beneficiary = beneficiary,
        description = description,
        amount = amount,
        transType = transType,
    )

    db.session.add(tran)
    db.session.commit()

    tr = Transaction.query.filter_by(account_id=acct_id).all()
    return jsonify({'data': tr, 'msg': 'Transaction saved', 'status': 'success'}), 201


