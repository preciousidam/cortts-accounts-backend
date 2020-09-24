from datetime import datetime as dt
from server.util.instances import db

class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    prop = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    area = db.Column(db.String(255), nullable=False)
    tenant = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=False)
    landlord = db.Column(db.Integer, db.ForeignKey('landlord.id'), nullable=False)
    rent = db.Column(db.String(255), nullable=False)
    serv_charge = db.Column(db.String(255), nullable=False)
    period = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    note = db.Column(db.String(1000), nullable=False)
    noOfBed = db.Column(db.Integer, nullable=False)
    noOfBath = db.Column(db.Integer, nullable=False)
    noOfToilet = db.Column(db.Integer, nullable=False)
    noOfPark = db.Column(db.Integer, nullable=False)
    furnished = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=dt.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=dt.now(), onupdate=dt.now())

    def __repr__(self):
        return 'Flat: %r' % self.name

    def json(self):
        return {
            'id': self.id, 
            "name": self.name,
            'prop': self.prop,
            'address': self.address,
            'area': self.area,
            'tenant': self.tenant,
            'landlord': self.landlord,
            'rent': self.rent,
            'serv_charge': self.serv_charge,
            'period': self.period,
            'status': self.status,
            'note': self.note,
            'noOfBed': self.noOfBed,
            'noOfBath': self.noOfBath,
            'noOfToilet': self.noOfToilet,
            'noOfPark': self.noOfPark,
            'furnished': self.furnished,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


