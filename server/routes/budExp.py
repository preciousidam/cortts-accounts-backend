from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from server.models.Budget import Budget, BudgetItem
from server.models.Expense import Expense, ExpenseItem
from server.models.ExpenseAccount import ExpenseAccount
from server.models.OtherModels import Category
from server.util.instances import db

budExpRoute = Blueprint('budExp', __name__,url_prefix='/api')

@budExpRoute.route('/budget/', methods=['GET'])
def get_all_budgets():
    budgets = Budget.query.all()
    return jsonify({'data': budgets, 'msg': 'success'}), 200


@budExpRoute.route('/budget/<path:path>', methods=['GET'])
def get_budget(path):
    budget = Budget.query.filter_by(id=path).first()
    return jsonify({'data': budget, 'msg': 'success'}), 200


@budExpRoute.route('/expense/', methods=['GET'])
def get_all_expenses():
    expenses = Expense.query.all()
    return jsonify({'data': expenses, 'msg': 'success'}), 200


@budExpRoute.route('/expense/<path:path>', methods=['GET'])
def get_expense(path):
    expense = Expense.query.filter_by(ref=path).first()
    return jsonify({'data': expense, 'msg': 'success'}), 200


@budExpRoute.route('/budget/create', methods=['POST'])
def create_budget():

    if request.method == 'POST':
        ref = request.json.get('ref')
        date = request.json.get('date')
        items = request.json.get('items')
        amount = request.json.get('amount')
        
        
    if not ref:
        return jsonify({'msg': 'Missing ref', 'status': 'failed'}), 400

    if not date:
        return jsonify({'msg': 'Missing date', 'status': 'failed'}), 400

    if not items:
        return jsonify({'msg': 'Missing items', 'status': 'failed'}), 400

    if not amount:
        return jsonify({'msg': 'Missing amount', 'status': 'failed'}), 400


    budget = Budget(
        date = date,
        ref = ref,
        amount = amount,
    )

    db.session.add(budget)
    db.session.commit()
    db.session.refresh(budget)

    for item in items:
        i = BudgetItem(
            budget_id=budget.id,
            description=item.get('desc'),
            quantity=item.get('qty'),
            amount=item.get('amount'),
        )
        db.session.add(i)

    db.session.commit()

    return jsonify({'msg': 'Budget saved', 'status': 'success'}), 201


@budExpRoute.route('/expense/create', methods=['POST'])
def create_expense():

    if request.method == 'POST':
        ref = request.json.get('ref')
        date = request.json.get('date')
        items = request.json.get('items')
        amount = request.json.get('amount')
        method = request.json.get('method')
        account = request.json.get('account')
        recipient = request.json.get('recipient')
        
        

    if not date:
        return jsonify({'msg': 'Missing date', 'status': 'failed'}), 400

    if not ref:
        return jsonify({'msg': 'Missing ref', 'status': 'failed'}), 400

    if not items:
        return jsonify({'msg': 'Missing items', 'status': 'failed'}), 400

    if not amount:
        return jsonify({'msg': 'Missing amount', 'status': 'failed'}), 400

    if not method:
        return jsonify({'msg': 'Missing method', 'status': 'failed'}), 400

    if not account:
        return jsonify({'msg': 'Missing account', 'status': 'failed'}), 400


    if not recipient:
        return jsonify({'msg': 'Missing recipient', 'status': 'failed'}), 400

    


    expense = Expense(
        date = date,
        ref = ref,
        amount = amount,
        payMethod = method,
        account = account,
        recipient = recipient
    )

    db.session.add(expense)
    db.session.commit()
    db.session.refresh(expense)


    for item in items:
        i = ExpenseItem(
            expense_id=expense.id,
            description=item.get('desc'),
            category=item.get('category_id'),
            amount=item.get('amount'),
            company=item.get('company')
        )
        db.session.add(i)

    acct = ExpenseAccount.query.filter_by(id=account).first()

    balance = float(acct.balance) - float(amount)

    acct.balance = "{:.2f}".format(balance)

    db.session.commit()

    return jsonify({'msg': 'Expenses saved', 'status': 'success'}), 201


@budExpRoute.route('/expense/edit', methods=['POST'])
def edit_expense():

    if request.method == 'POST':
        id = request.json.get('id')
        ref = request.json.get('ref')
        date = request.json.get('date')
        items = request.json.get('items')
        amount = request.json.get('amount')
        account = request.json.get('account')
        method = request.json.get('payMethod')
        delete = request.json.get('deletedItem')
        recipient = request.json.get('recipient')
        
        

    if not date:
        return jsonify({'msg': 'Missing date', 'status': 'failed'}), 400

    if not ref:
        return jsonify({'msg': 'Missing ref', 'status': 'failed'}), 400
    
    if not id:
        return jsonify({'msg': 'Missing id', 'status': 'failed'}), 400

    if not items:
        return jsonify({'msg': 'Missing items', 'status': 'failed'}), 400

    if not amount:
        return jsonify({'msg': 'Missing amount', 'status': 'failed'}), 400

    if not method:
        return jsonify({'msg': 'Missing method', 'status': 'failed'}), 400

    if not account:
        return jsonify({'msg': 'Missing account', 'status': 'failed'}), 400


    if not recipient:
        return jsonify({'msg': 'Missing recipient', 'status': 'failed'}), 400

    
    expense = Expense.query.filter_by(id=id).first()

    diff = float(expense.amount) - float(amount)

    expense.amount = amount

    for item in items:
        if 'id' in item:
            exp = ExpenseItem.query.filter_by(id=item['id']).update(dict(
                description=item.get('description'),
                category=item.get('category'),
                amount=item.get('amount'),
                company=item.get('company'),
                expense_id=id,
            ))
            
        else:
            i = ExpenseItem(
                expense_id=id,
                description=item.get('description'),
                category=item.get('category'),
                amount=item.get('amount'),
                company=item.get('company')
            )
            db.session.add(i)
            
    
    if len(delete) != 0:
        for item in delete:
            ExpenseItem.query.filter_by(id=item['id']).delete()


    acct = ExpenseAccount.query.filter_by(id=account).first()
    acct.balance = "{:.2f}".format(float(acct.balance)-diff)
    db.session.commit()

    return jsonify({'msg': 'Expenses saved', 'status': 'success'}), 201



@budExpRoute.route('/budget/delete', methods=['POST'])
@jwt_required
def delete_budgets():
    id = None
    

    if request.method == 'POST':
        id = request.json.get('id')
    

    if not id:
        return jsonify({'msg': 'Missing Budget ID', 'status': 'failed'}), 400

    

    Budget.query.filter_by(id=id).delete()

    db.session.commit()


    budget = Budget.query.all()
    return jsonify({'data': budget, 'msg': 'Budget deleted', 'status': 'success'}), 201


@budExpRoute.route('/expense/delete', methods=['POST'])
@jwt_required
def delete_expenses():

    if request.method == 'POST':
        id = request.json.get('id')
    

    if not id:
        return jsonify({'msg': 'Missing Expense ID', 'status': 'failed'}), 400

    

    exp = Expense.query.filter_by(id=id).first()
    db.session.delete(exp)
    db.session.commit()


    expense = Expense.query.all()
    return jsonify({'data': expense, 'msg': 'Expenses deleted', 'status': 'success'}), 201


@budExpRoute.route('/expense/summary', methods=['GET'])
def summarize_expenses():
    categories = Category.query.all()
    expenses = ExpenseItem.query.all()

    data = []

    for cat in categories:
        exp = [item for item in expenses if item.category == cat.id]
        data.append({'category': cat, 'items': exp})

    return jsonify({'data': data, 'msg': 'success'}), 200