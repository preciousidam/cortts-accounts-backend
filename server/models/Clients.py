from datetime import datetime as dt
from server.util.instances import db
from server.models.Flat import Flat

class Landlord(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    contactPerson = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    flat = db.relationship('Flat', backref='Landlord', lazy=True)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())


    def __repr__(self): 
        return 'Landlord %r' % self.name

    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'email': self.email,
            'contact_person': self.contactPerson,
            'phone': self.phone,
            'flat': self.flat, 
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class Tenant(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    contactPerson = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    flat = db.relationship('Flat', backref='Tenant', lazy=True)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())


    def __repr__(self): 
        return 'Tenant: %r' % self.name

    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'email': self.email,
            'contact_person': self.contactPerson,
            'phone': self.phone,
            'flat': self.flat, 
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    
    