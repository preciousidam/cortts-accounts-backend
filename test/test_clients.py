import pytest

from server.models.Clients import Landlord, Tenant
from server.util.instances import db


@pytest.fixture
def createLandlord(app, client):

    with app.app_context():
        db.create_all()
        landlord = Landlord(
            name='name',
            email='email',
            address='address',
            phone='phone',
            contactPerson='contactPerson',
        )
    
        db.session.add(landlord)
        db.session.commit()

    data = dict(email='ebube@cortts.com',password='lilian01')
    resp = client.post('/api/auth/login', json=data)
    json = resp.get_json()
    yield json['token']

@pytest.fixture
def createTenant(app, client):
    
    with app.app_context():
        db.create_all()
        tenant = Tenant(
            name='name',
            email='email',
            address='address',
            phone='phone',
            contactPerson='contactPerson',
        )
    
        db.session.add(tenant)
        db.session.commit()

    data = dict(email='ebube@cortts.com',password='lilian01')
    resp = client.post('/api/auth/login', json=data)
    json = resp.get_json()
    yield json['token']


def test_fetch_client_l(client, createLandlord):
   
    resp = client.get('/api/landlords/')
    json = resp.get_json()
    assert resp.status_code == 200

    assert isinstance(json['data'],list)
    assert isinstance(json['data'][0],dict)

    resp = client.get('/api/landlords/1')
    json = resp.get_json()
    assert resp.status_code == 200

    assert isinstance(json['data'],dict)


def test_fetch_client_t(client, createTenant):
   
    resp = client.get('/api/tenants/')
    json = resp.get_json()
    assert resp.status_code == 200

    assert isinstance(json['data'],list)
    assert isinstance(json['data'][0],dict)

    resp = client.get('/api/tenants/1')
    json = resp.get_json()
    assert resp.status_code == 200

    assert isinstance(json['data'],dict)
    


@pytest.mark.parametrize(
    ("name", "email", "phone", "address", "contactPerson", "message"),
    (
        ("", "", "", "", "", "Missing Landlord Name"),
        ("ebube@cortts.com", "", "", "", "", "Missing Landlord Email"),
        ("ebube@cortts.com", "something", "c", "", "", "Missing Landlord Address"),
        ("ebube@cortts.com", "something", "", "c", "", "Missing Landlord Phone"),
        ("ebube@cortts.com", "something", "c", "08162300796", "", "Missing Landlord Contact Person"),
    ),
)
def test_validate_client_l_param(client, createLandlord, name, email, phone, address, contactPerson, message):
    data = dict(
        name=name,
        email=email,
        address=address,
        phone=phone,
        contactPerson=contactPerson,
    )
    headers = {'Authorization': 'Bearer {}'.format(createLandlord)}
    resp = client.post('/api/landlords/create', json=data, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 400

    assert json['status'] == 'failed'
    assert message in json['msg']


@pytest.mark.parametrize(
    ("name", "email", "phone", "address", "contactPerson", "message"),
    (
        ("", "", "", "", "", "Missing Tenant Name"),
        ("ebube@cortts.com", "", "", "", "", "Missing Tenant Email"),
        ("ebube@cortts.com", "something", "c", "", "", "Missing Tenant Address"),
        ("ebube@cortts.com", "something", "", "c", "", "Missing Tenant Phone"),
        ("ebube@cortts.com", "something", "c", "08162300796", "", "Missing Tenant Contact Person"),
    ),
)
def test_validate_client_t_param(client, createTenant, name, email, phone, address, contactPerson, message):
    data = dict(
        name=name,
        email=email,
        address=address,
        phone=phone,
        contactPerson=contactPerson,
    )
    headers = {'Authorization': 'Bearer {}'.format(createTenant)}
    resp = client.post('/api/tenants/create', json=data, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 400

    assert json['status'] == 'failed'
    assert message in json['msg']


@pytest.mark.parametrize(
    ("name", "email", "phone", "address", "contactPerson", "message"),
    (
        ("ebube@cortts.com", "something", "c", "08162300796", "d", "Tenant saved"),
    ),
)
def test_create_client_t_param(client, createLandlord, name, email, phone, address, contactPerson, message):
    data = dict(
        name=name,
        email=email,
        address=address,
        phone=phone,
        contactPerson=contactPerson,
    )
    headers = {'Authorization': 'Bearer {}'.format(createLandlord)}
    resp = client.post('/api/tenants/create', json=data, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 201

    assert json['status'] == 'success'
    assert message in json['msg']
    assert isinstance(json['data'], list)

@pytest.mark.parametrize(
    ("name", "email", "phone", "address", "contactPerson", "message"),
    (
        ("ebube@cortts.com", "something", "c", "08162300796", "d", "Landlord saved"),
    ),
)
def test_create_client_l_param(client, createLandlord, name, email, phone, address, contactPerson, message):
    data = dict(
        name=name,
        email=email,
        address=address,
        phone=phone,
        contactPerson=contactPerson,
    )
    headers = {'Authorization': 'Bearer {}'.format(createLandlord)}
    resp = client.post('/api/landlords/create', json=data, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 201

    assert json['status'] == 'success'
    assert message in json['msg']
    assert isinstance(json['data'], list)



@pytest.mark.parametrize(
    ("id", "name", "email", "phone", "address", "contactPerson", "message"),
    (
        (1, "ebube1@cortts.com", "something", "c", "08162300796", "d", "Landlord saved"),
    ),
)
def test_edit_client_l_param(client, createLandlord, id, name, email, phone, address, contactPerson, message):
    data = dict(
        id=id,
        name=name,
        email=email,
        address=address,
        phone=phone,
        contactPerson=contactPerson,
    )
    headers = {'Authorization': 'Bearer {}'.format(createLandlord)}
    resp = client.post('/api/landlords/edit', json=data, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 201

    assert json['status'] == 'success'
    assert message in json['msg']
    assert isinstance(json['data'], dict)
    assert json['data']['email'] == email


@pytest.mark.parametrize(
    ("id", "name", "email", "phone", "address", "contactPerson", "message"),
    (
        (1, "ebube1@cortts.com", "something", "c", "08162300796", "d", "Tenant saved"),
    ),
)
def test_edit_client_t_param(client, createTenant, id, name, email, phone, address, contactPerson, message):
    data = dict(
        id=id,
        name=name,
        email=email,
        address=address,
        phone=phone,
        contactPerson=contactPerson,
    )
    headers = {'Authorization': 'Bearer {}'.format(createTenant)}
    resp = client.post('/api/tenants/edit', json=data, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 201

    assert json['status'] == 'success'
    assert message in json['msg']
    assert isinstance(json['data'], dict)
    assert json['data']['email'] == email

    
def test_delete_client_l(app, client, createLandlord):
    headers = {'Authorization': 'Bearer {}'.format(createLandlord)}
    resp = client.post('/api/landlords/delete', json={'id': 1}, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 201

    assert json['status'] == 'success'
    assert 'Landlord deleted' in json['msg']
    with app.app_context():
        assert Landlord.query.count() <= 0


def test_delete_client_t(app, client, createTenant):
    headers = {'Authorization': 'Bearer {}'.format(createTenant)}
    resp = client.post('/api/tenants/delete', json={'id': 1}, headers=headers)
    json = resp.get_json()
    assert resp.status_code == 201

    assert json['status'] == 'success'
    assert 'Tenant deleted' in json['msg']
    with app.app_context():
        assert Tenant.query.count() <= 0



    

    