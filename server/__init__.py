import os
from flask import Flask, render_template
from flask_cors import CORS

from server.models.User import User
from server.models.Account import Account
from server.models.Transactions import Transaction
from server.models.Budget import Budget, BudgetItem
from server.models.Expense import Expense, ExpenseItem
from server.models.ExpenseAccount import ExpenseAccount, ExpenseAccountHistory
from server.models.OtherModels import Category, Staff
from server.util.instances import db, initializeDB, initializeJWT
from server.routes.auth import authRoute
from server.routes.account import accountsRoute
from server.routes.transaction import transRoute
from server.routes.budExp import budExpRoute
from server.routes.expenseAcct import expAcctRoute
from server.routes.otherroutes import otherRoute
from server.util.jsonEncoder import JSONEncoder
    


def create_app(test_config=None):
    # create and configure the app
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
   
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config.DevelopementConfig')
        
    else:
        # load the test config if passed in
        app.config.from_object('config.TestConfig')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #initialize Database
    initializeDB(app)

    #initialize JWT 
    initializeJWT(app)
   
    '''change jsonify default JSON encoder to a custom Encode
    ### to support Model encoding for {user, account, transaction, etc}
    '''
    app.json_encoder = JSONEncoder


    #Register Blueprints
    app.register_blueprint(authRoute)
    app.register_blueprint(accountsRoute)
    app.register_blueprint(budExpRoute)
    app.register_blueprint(expAcctRoute)
    app.register_blueprint(transRoute)
    app.register_blueprint(otherRoute)

    @app.route('/createDB')
    def create():
        
        db.create_all()
        db.session.commit()
        return 'ok'

    @app.route('/addUserToDB')
    def addUser():
        user = User(username="EbubeIdam", 
                    name="Ebube Idam", 
                    email="ebube@cortts.com", 
                    phone="08162300796", 
                    password="pbkdf2:sha256:150000$eGO8fIQ6$8c390d52bd557b4e3a4e1521efe103be9a5cb9cb4db3d0d2dfe3cc29e40ecd41")
        
        #db.create_all()
        db.session.add(user)
        db.session.commit()
        return 'ok'

    @app.route('/addAcctToDB')
    def addAcct():
        accts = [{'name': "Cortts Real", 'number': "1100112233", 'sort_code': '123456', 'balance': '240657000.29', 'bank': "Access Bank"},
                {'name': "Cortts Real", 'number': "1890112233", 'sort_code': '123236', 'balance': '100657000.92', 'bank': "Access Bank"},
                {'name': "Cortts Limited", 'number': "1198712200", 'sort_code': '123896', 'balance': '240907000.10', 'bank': "Zenith Bank"},
                {'name': "Cortts Limited", 'number': "1131192331", 'sort_code': '129756', 'balance': '240657000.29', 'bank': "Zenith Bank"},]
        
        
        for acct in accts:
            x = Account(name=acct['name'], 
                        number=acct['number'], 
                        sort_code=acct['sort_code'],
                        balance=acct['balance'],
                        bank=acct['bank'])
            #db.create_all()
            db.session.add(x)
            db.session.commit()
            
        return 'ok'

    @app.route('/addCatToDB')
    def addcategory():
        cats = [
                    {'id': 1, 'name': 'Transportation'},
                    {'id': 2, 'name': 'Utility'},
                    {'id': 3, 'name': 'Medical Expenses'},
                    {'id': 4, 'name': 'office expenses'},
                    {'id': 5, 'name': 'Telecommunication'},
                    {'id': 6, 'name': 'Meal Entertainment'},
                ]
        
        
        for cat in cats:
            x = Category(title=cat['name'])
            #db.create_all()
            db.session.add(x)
            db.session.commit()
            
        return 'ok'

    @app.route('/addStaffToDB')
    def addstaff():
        staff = [
                    {'id': 1, 'name': 'Madam Stella'},
                    {'id': 2, 'name': 'Madam Aminat'},
                    {'id': 3, 'name': 'Ebube'},
                    {'id': 4, 'name': 'Christy'},
                    {'id': 5, 'name': 'Godwin'},
                    {'id': 6, 'name': 'Anita'},
                ]
        
        
        for staf in staff:
            x = Staff(name=staf['name'])
            #db.create_all()
            db.session.add(x)
            db.session.commit()
            
        return 'ok'

    @app.route('/addPettyToDB')
    def addPetty():
        
        x = ExpenseAccount(
            name = "Impress",
            balance = "250000.00"
        )
        
        #db.create_all()
        db.session.add(x)
        db.session.commit()
            
        return 'ok'


    #initialize CORS
    CORS(app)
    return app