from server.util.instances import db
from datetime import datetime as dt


class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.String(120), nullable=False)
    ref = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.String(255), nullable=False)
    items = db.relationship('BudgetItem', cascade='all, delete, delete-orphan', backref='budget', lazy=False, passive_deletes=True)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())


    def __repr__(self):
        return 'Budget for %r' % self.date

    
    def json(self):
        return {
            'id': self.id,
            'date': self.date,
            'ref': self.ref,
            'amount': self.amount,
            'items': self.items,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }





class BudgetItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id', ondelete='CASCADE'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())

    def __repr__(self):
        return 'Item in budget for %r' % self.date

    def json(self):
        return {
            'id': self.id,
            'budget': self.budget_id,
            'description': self.description,
            'quantity': self.quantity,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }