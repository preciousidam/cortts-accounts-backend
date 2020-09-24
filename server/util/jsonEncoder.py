from flask.json import JSONEncoder
from datetime import datetime as dt

from server.models.Account import Account
from server.models.Transactions import Transaction
from server.models.User import User
from server.models.Budget import Budget, BudgetItem
from server.models.Expense import Expense, ExpenseItem
from server.models.ExpenseAccount import ExpenseAccount, ExpenseAccountHistory
from server.models.OtherModels import Category, Staff

class JSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Account) or isinstance(obj, Transaction) or isinstance(obj, User):
            return obj.json()

        if isinstance(obj, Budget) or isinstance(obj,BudgetItem):
            return obj.json()
            
        if isinstance(obj, Expense) or isinstance(obj, ExpenseItem):
            return obj.json()

        if isinstance(obj, ExpenseAccount) or isinstance(obj, ExpenseAccountHistory):
            return obj.json()

        if isinstance(obj, Category) or isinstance(obj, Staff):
            return obj.json()

        if isinstance(obj, dt):
            #return o.strftime("%Y-%m-%d %H:%M:%S")
            return obj.strftime("%d-%m-%Y")

        return JSONEncoder.default(self, obj)