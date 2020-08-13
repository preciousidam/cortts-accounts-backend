from flask.json import JSONEncoder
from datetime import datetime as dt

from server.models.Account import Account
from server.models.Transactions import Transaction
from server.models.User import User

class JSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Account) or isinstance(obj, Transaction) or isinstance(obj, User):
            return obj.json()
            
        if isinstance(obj, dt):
            #return o.strftime("%Y-%m-%d %H:%M:%S")
            return obj.strftime("%Y-%m-%d")

        return JSONEncoder.default(self, obj)