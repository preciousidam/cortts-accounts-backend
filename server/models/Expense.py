from server.util.instances import db
from datetime import datetime as dt


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.String(120), nullable=False)
    recipient = db.Column(db.String(255), nullable=False)
    account = db.Column(db.String(255), nullable=False)
    payMethod = db.Column(db.String(255), nullable=True)
    ref = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.String(255), default="", nullable=False)
    items = db.relationship('ExpenseItem',cascade='all, delete, delete-orphan', backref='expense', lazy=False, passive_deletes=True)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())


    def __repr__(self):
        return 'Budget for %r' % self.date

    
    def json(self):
        return {
            'id': self.id,
            'date': self.date,
            'recipient': self.recipient,
            'account': self.account,
            'payMethod': self.payMethod,
            'ref': self.ref,
            'amount': self.amount,
            'items': self.items,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }





class ExpenseItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    expense_id = db.Column(db.Integer, db.ForeignKey('expense.id', ondelete='CASCADE'), nullable=False)
    category = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=True)
    amount = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())

    def __repr__(self):
        return 'Item in expenses for %r' % self.date

    def json(self):
        return {
            'id': self.id,
            'expense': self.expense_id,
            'category': self.category,
            'description': self.description,
            'company': self.company,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }