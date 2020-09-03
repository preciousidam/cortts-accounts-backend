from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from server.models.Budget import Budget, BudgetItem
from server.models.ExpenseAccount import ExpenseAccount, ExpenseAccountHistory
from server.util.instances import db

expAcctRoute = Blueprint('expenseacct', __name__,url_prefix='/api/expense/account')

@expAcctRoute.route('/', methods=['GET'])
def get_all_accounts():
    accounts = ExpenseAccount.query.all()
    return jsonify({'data': accounts, 'msg': 'success'}), 200

@expAcctRoute.route('/<path:path>', methods=['GET'])
def get_account(path):
    account = ExpenseAccount.query.filter_by(id=path).first()
    return jsonify({'data': account, 'msg': 'success'}), 200


@expAcctRoute.route('/create', methods=['POST'])
@jwt_required
def create_account():
    
    if request.method == 'POST':
        name = request.json.get('title')
        amount = request.json.get('balance')
        

    if not name:
        return jsonify({'msg': 'Missing Acct title', 'status': 'failed'}), 400

    if not amount:
        return jsonify({'msg': 'Missing opening balance', 'status': 'failed'}), 400




    acct = ExpenseAccount(
        name = name,
        balance = amount,
    )

    db.session.add(acct)
    db.session.commit()
    db.session.refresh(acct)

    return jsonify({'data': acct, 'msg': 'Account created', 'status': 'success'}), 201


@expAcctRoute.route('/delete', methods=['POST'])
@jwt_required
def delete_account():
    
    if request.method == 'POST':
        id = request.json.get('id')
    

    if not id:
        return jsonify({'msg': 'Missing Account ID', 'status': 'failed'}), 400

    

    ExpenseAccount.query.filter_by(id=id).delete()

    db.session.commit()


    accts = ExpenseAccount.query.all()
    return jsonify({'data': accts, 'msg': 'Account deleted', 'status': 'success'}), 201



@expAcctRoute.route('/fund', methods=['POST'])
@jwt_required
def fund_account():
    
    if request.method == 'POST':
        acct_id = request.json.get('acct_id')
        amount = request.json.get('balance')
        

    if not acct_id:
        return jsonify({'msg': 'Missing Acct Id', 'status': 'failed'}), 400

    if not amount:
        return jsonify({'msg': 'Missing amount', 'status': 'failed'}), 400




    exp = ExpenseAccount.query.filter_by(id=acct_id).first()

    exp.balance = "{:.2f}".format(float(exp.balance) + float(amount))
    
    db.session.commit()

    db.session.refresh(exp)

    return jsonify({'data': exp, 'msg': 'Account funded', 'status': 'success'}), 201