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
from server.models.Clients import Landlord, Tenant
from server.models.Flat import Flat
from server.models.OtherAccounts import OtherAccount
from server.util.instances import db, initializeDB, initializeJWT
from server.routes.auth import authRoute
from server.routes.account import accountsRoute
from server.routes.transaction import transRoute
from server.routes.budExp import budExpRoute
from server.routes.expenseAcct import expAcctRoute
from server.routes.otherroutes import otherRoute
from server.routes.landlord import landlordsRoute
from server.routes.tenant import tenantsRoute
from server.routes.flat import flatsRoute
from server.util.jsonEncoder import JSONEncoder
    

#create_app(test_config=None):
def create_app(env):
    # create and configure the app
    
    app = Flask(__name__, instance_relative_config=True)
   
    if env == 'development':
        # load the instance dev config, if it exists, when not testing
        app.config.from_object('instance.config.DevelopementConfig')

    elif env == 'production':
        # load the instance production config, if it exists, when not testing
        app.config.from_object('instance.config.ProductionConfig')
        
    elif env == 'testing':
        # load the test config if passed in
        app.config.from_object('instance.config.TestConfig')

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
    app.register_blueprint(landlordsRoute)
    app.register_blueprint(tenantsRoute)
    app.register_blueprint(flatsRoute)

    @app.route('/createDB')
    def create():
        
        db.create_all()
        db.session.commit()
        return 'ok'


    #initialize CORS
    CORS(app)
    return app