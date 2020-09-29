import pytest

from server.models.Flat import Flat
from server.util.instances import db
from data import get_params


@pytest.fixture
def createFlat(app, client):

    with app.app_context():
        db.create_all()
        flat = Flat(
            name = 'name',
            prop = 'prop',
            address = 'address',
            area = 'area',
            tenant = 'tenant',
            landlord = 'landlord',
            rent = 'rent',
            serv_charge = 'serv_charge',
            period = 'period',
            status = 'status',
            note = 'note',
            noOfBed = 'noOfBed',
            noOfBath = 'noOfBath',
            noOfToilet = 'noOfToilet',
            noOfPark = 'noOfPark',
            furnished = True,
        )
    
        db.session.add(flat)
        db.session.commit()

    data = dict(email='ebube@cortts.com',password='lilian01')
    resp = client.post('/api/auth/login', json=data)
    json = resp.get_json()
    yield json['token']



def test_fetch_flat(client, createFlat):
   
    resp = client.get('/api/flats/')
    json = resp.get_json()
    assert resp.status_code == 200

    assert isinstance(json['data'],list)
    assert isinstance(json['data'][0],dict)

    resp = client.get('/api/flats/1')
    json = resp.get_json()
    assert resp.status_code == 200

    assert isinstance(json['data'],dict)



@pytest.mark.parametrize(
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 
    'landlord', 'period', 'status', 'furnished', 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'message'),
    get_params(),
)
def test_validate_flat_param(client, createFlat, name, prop, address, area, rent, serv_charge, tenant, 
    landlord, period, status, furnished, noOfBed, noOfBath, noOfPark, noOfToilet, message):
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
        noOfBed = noOfBed,
        noOfBath = noOfBath,
        noOfToilet = noOfToilet,
        noOfPark = noOfPark,
        furnished = furnished,
    )
    headers = {'Authorization': 'Bearer {}'.format(createFlat)}
    resp = client.post('/api/flats/create', json=data, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 400

    assert json['status'] == 'failed'
    assert message in json['msg']



@pytest.mark.parametrize(
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 
    'landlord', 'period', 'status', 'furnished', 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'message'),
    (
        ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 
        'landlord', 'period', 'status', True, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Flat saved'),
    ),
)
def test_create_flat_param(client, createFlat, name, prop, address, area, rent, serv_charge, tenant, 
    landlord, period, status, furnished, noOfBed, noOfBath, noOfPark, noOfToilet, message):
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
        noOfBed = noOfBed,
        noOfBath = noOfBath,
        noOfToilet = noOfToilet,
        noOfPark = noOfPark,
        furnished = furnished,
    )
    print(data)
    headers = {'Authorization': 'Bearer {}'.format(createFlat)}
    resp = client.post('/api/flats/create', json=data, headers=headers)
    json = resp.get_json()
    print(json)
    assert resp.status_code == 201
    
    assert json['status'] == 'success'
    assert message in json['msg']
    assert isinstance(json['data'], list)



@pytest.mark.parametrize(
    ("name", "prop", "address", "area", "rent", "serv_charge", 'tenant', 
    'landlord', 'period', 'status', 'furnished', 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'message'),
    (
        ("AM6", "prop", "address", "area", "rent", "serv_charge", 'flour mill', 'modd family', 'period', 'status', 
        True, 'noOfBed', 'noOfBath', 'noOfPark', 'noOfToilet', 'Flat details saved'),
    ),
)
def test_edit_flat_param(client, createFlat, name, prop, address, area, rent, serv_charge, tenant, 
                            landlord, period, status, furnished, noOfBed, noOfBath, noOfPark, noOfToilet, message):
    data = dict(
        id=1,
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
        noOfBed = noOfBed,
        noOfBath = noOfBath,
        noOfToilet = noOfToilet,
        noOfPark = noOfPark,
        furnished = furnished,
        note = 'note',
    )
    headers = {'Authorization': 'Bearer {}'.format(createFlat)}
    resp = client.post('/api/flats/edit', json=data, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 201

    assert json['status'] == 'success'
    assert message in json['msg']
    assert isinstance(json['data'], dict)
    assert json['data']['name'] == name
    assert json['data']['landlord'] == landlord
    assert json['data']['tenant'] == tenant
    assert json['data']['furnished'] == furnished


    
def test_delete_flat(app, client, createFlat):
    headers = {'Authorization': 'Bearer {}'.format(createFlat)}
    resp = client.post('/api/flats/delete', json={'id': 1}, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 201

    assert json['status'] == 'success'
    assert 'Flat deleted' in json['msg']
    with app.app_context():
        assert Flat.query.count() <= 0  



    

    