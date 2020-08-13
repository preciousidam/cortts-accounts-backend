from server.util.instances import db
from datetime import datetime as dt

from server.models.Transactions import Transaction

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    number = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    sort_code = db.Column(db.String(10), nullable=False)
    balance = db.Column(db.String(25), nullable=False)
    bank = db.Column(db.String(255), nullable=False)
    transactions = db.relationship(Transaction, backref='account', lazy=False)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())


    def __repr__(self):
        return 'Account %r %r %r' % self.number, self.name, self.bank

    
    def json(self):
        return {
            'id': self.id,
            'number': self.number,
            'name': self.name,
            'sort_code': self.sort_code,
            'balance': self.balance,
            'bank': self.bank,
            'transactions': self.transactions,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
