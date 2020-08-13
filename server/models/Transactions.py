from server.util.instances import db
from datetime import datetime as dt


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.String(120), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    beneficiary = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    transType = db.Column(db.String(11), nullable=False)
    amount = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())


    def __repr__(self):
        return 'Transaction %r' % self.id

    
    def json(self):
        return {
            'id': self.id,
            'date': self.date,
            'account': self.account_id,
            'beneficiary': self.beneficiary,
            'description': self.description,
            'transType': self.transType,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
