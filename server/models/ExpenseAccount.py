from server.util.instances import db
from datetime import datetime as dt


class ExpenseAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    balance = db.Column(db.String(255), nullable=False)
    history = db.relationship('ExpenseAccountHistory', backref='expense_account', lazy=False)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())


    def __repr__(self):
        return '%r Expense Account' % self.name

    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'balance': self.balance,
            'history': self.history,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class ExpenseAccountHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user = db.Column(db.String(255), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('expense_account.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False, default="Expense account credited")
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())


    def __repr__(self):
        return 'Expense transaction history at %r' % self.created_at

    
    def json(self):
        return {
            'id': self.id,
            'account': self.account_id,
            'user': self.user,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }