from flask import Blueprint, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import jwt_required

from server.models.Flat import Flat
from server.util.instances import db


flatsRoute = Blueprint('flats', __name__,url_prefix='/api/flats')

@flatsRoute.route('/', methods=['GET'])
def get_all_flats():
    flats = Flat.query.all()
    return jsonify({'data': flats, 'msg': 'success'}), 200


@flatsRoute.route('/<path:path>', methods=['GET'])
def get_account(path):
    flats = Flat.query.filter_by(id=path).first()
    return jsonify({'data': flats, 'msg': 'success'}), 200


@flatsRoute.route('/create', methods=['POST'])
@jwt_required
def create_flats():

    if request.method == 'POST':
        name = request.json.get('name')
        prop = request.json.get('prop')
        address = request.json.get('address')
        area = request.json.get('area')
        tenant = request.json.get('tenant')
        landlord = request.json.get('landlord')
        rent = request.json.get('rent')
        serv_charge = request.json.get('serv_charge')
        period = request.json.get('period')
        status = request.json.get('status')
        note = request.json.get('note')
        noOfBed = request.json.get('noOfBed')
        noOfBath = request.json.get('noOfBath')
        noOfToilet = request.json.get('noOfToilet')
        noOfPark = request.json.get('noOfPark')
        furnished = request.json.get('furnished')

    if not name:
        return jsonify({'msg': 'Missing Flat title', 'status': 'failed'}), 400

    if not prop:
        return jsonify({'msg': 'Missing Property', 'status': 'failed'}), 400

    if not address:
        return jsonify({'msg': 'Missing Address', 'status': 'failed'}), 400

    if not area:
        return jsonify({'msg': 'Missing Area', 'status': 'failed'}), 400

    if not rent:
        return jsonify({'msg': 'Missing Flat rent', 'status': 'failed'}), 400

    if not serv_charge:
        return jsonify({'msg': 'Missing service charge', 'status': 'failed'}), 400

    if not tenant:
        return jsonify({'msg': 'Missing Flat tenant', 'status': 'failed'}), 400

    if not landlord:
        return jsonify({'msg': 'Missing Flat landlord', 'status': 'failed'}), 400

    if not period:
        return jsonify({'msg': 'Missing tenancy period', 'status': 'failed'}), 400

    if not status:
        return jsonify({'msg': 'Missing Flat status', 'status': 'failed'}), 400
        

    if not furnished:
        return jsonify({'msg': 'Missing Furnished', 'status': 'failed'}), 400



    if not noOfBath:
        return jsonify({'msg': 'Missing No. of Bathrooms', 'status': 'failed'}), 400

    if not noOfBed:
        return jsonify({'msg': 'Missing number of bedroom', 'status': 'failed'}), 400

    if not noOfPark:
        return jsonify({'msg': 'Missing number of park', 'status': 'failed'}), 400

    if not noOfToilet:
        return jsonify({'msg': 'Missing number of toilet', 'status': 'failed'}), 400


    flat = Flat(
        name = name,
        prop = prop,
        address = address,
        area = area,
        tenant = tenant,
        landlord = landlord,
        rent = rent,
        serv_charge = serv_charge,
        period = period,
        status = status,
        note = note,
        noOfBed = noOfBed,
        noOfBath = noOfBath,
        noOfToilet = noOfToilet,
        noOfPark = noOfPark,
        furnished = furnished,
    )

    db.session.add(flat)
    db.session.commit()


    flats = Flat.query.all()
    return jsonify({'data': flats, 'msg': 'Flat saved', 'status': 'success'}), 201


@flatsRoute.route('/edit', methods=['POST'])
@jwt_required
def edit_flats():

    if request.method == 'POST':
        id = request.json.get('id')
        name = request.json.get('name')
        prop = request.json.get('prop')
        address = request.json.get('address')
        area = request.json.get('area')
        tenant = request.json.get('tenant')
        landlord = request.json.get('landlord')
        rent = request.json.get('rent')
        serv_charge = request.json.get('serv_charge')
        period = request.json.get('period')
        status = request.json.get('status')
        note = request.json.get('note')
        noOfBed = request.json.get('noOfBed')
        noOfBath = request.json.get('noOfBath')
        noOfToilet = request.json.get('noOfToilet')
        noOfPark = request.json.get('noOfPark')
        furnished = request.json.get('furnished')

    if not id:
        return jsonify({'msg': 'Missing Flat ID', 'status': 'failed'}), 400

    if not name:
        return jsonify({'msg': 'Missing Flat title', 'status': 'failed'}), 400

    if not prop:
        return jsonify({'msg': 'Missing Property', 'status': 'failed'}), 400

    if not address:
        return jsonify({'msg': 'Missing Address', 'status': 'failed'}), 400

    if not area:
        return jsonify({'msg': 'Missing Area', 'status': 'failed'}), 400

    if not rent:
        return jsonify({'msg': 'Missing Flat rent', 'status': 'failed'}), 400

    if not serv_charge:
        return jsonify({'msg': 'Missing service charge', 'status': 'failed'}), 400

    if not tenant:
        return jsonify({'msg': 'Missing Flat tenant', 'status': 'failed'}), 400

    if not landlord:
        return jsonify({'msg': 'Missing Flat landlord', 'status': 'failed'}), 400

    if not period:
        return jsonify({'msg': 'Missing tenancy period', 'status': 'failed'}), 400

    if not status:
        return jsonify({'msg': 'Missing Flat status', 'status': 'failed'}), 400
        

    if not furnished:
        return jsonify({'msg': 'Missing Furnished', 'status': 'failed'}), 400


    if not noOfBath:
        return jsonify({'msg': 'Missing No. of Bathrooms', 'status': 'failed'}), 400

    if not noOfBed:
        return jsonify({'msg': 'Missing number of bedroom', 'status': 'failed'}), 400

    if not noOfPark:
        return jsonify({'msg': 'Missing number of park', 'status': 'failed'}), 400

    if not noOfToilet:
        return jsonify({'msg': 'Missing number of toilet', 'status': 'failed'}), 400



    data = dict(
        name = name,
        prop = prop,
        address = address,
        area = area,
        tenant = tenant,
        landlord = landlord,
        rent = rent,
        serv_charge = serv_charge,
        period = period,
        status = status,
        note = note,
        noOfBed = noOfBed,
        noOfBath = noOfBath,
        noOfToilet = noOfToilet,
        noOfPark = noOfPark,
        furnished = furnished,
    )

    Flat.query.filter_by(id=id).update(data)
    db.session.commit()
    flat = Flat.query.filter_by(id=id).first()
    


    return jsonify({'data': flat, 'msg': 'Flat details saved', 'status': 'success'}), 201


@flatsRoute.route('/delete', methods=['POST'])
@jwt_required
def delete_flats():
   
    if request.method == 'POST':
        id = request.json.get('id')
    

    if not id:
        return jsonify({'msg': 'Missing Flat ID', 'status': 'failed'}), 400

    

    Flat.query.filter_by(id=id).delete()

    db.session.commit()


    flats = Flat.query.all()
    return jsonify({'data': flats, 'msg': 'Flat deleted', 'status': 'success'}), 201

