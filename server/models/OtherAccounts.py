from server.util.instances import db
from datetime import datetime as dt


class OtherAccount(db.Model):
    __tablename__ = 'otheraccounts'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    number = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    owner = db.Column(db.String(255), nullable=False)
    sort_code = db.Column(db.String(10), nullable=False)
    bank = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())


    def __repr__(self):
        return 'Account details for %r' % self.owner

    
    def json(self):
        return {
            'id': self.id,
            'number': self.number,
            'name': self.name,
            'sort_code': self.sort_code,
            'owner': self.owner,
            'bank': self.bank,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
