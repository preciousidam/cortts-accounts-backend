import pytest

from server.models.User import User
from server.util.instances import db


def test_login(client, app):
   
    resp = client.post('/api/auth/login', json={'email': 'ebube@cortts.com', 'password': 'lilian01'})
    json = resp.get_json()
    assert resp.status_code == 200

    assert json['status'] == 'success'
    assert 'token' in json
    assert 'refreshToken' in json


@pytest.mark.parametrize(
    ("email", "password", "message"),
    (
        ("", "", "Email not provided"),
        ("ebube@cortts.com", "", "Password not provided"),
    ),
)
def test_login_validate_param(client, app, email, password, message):
   
    resp = client.post('/api/auth/login', json=dict(email=email,password=password))
    json = resp.get_json()
    assert resp.status_code == 400

    assert json['status'] == 'error'
    assert message in json['msg']


@pytest.mark.parametrize(
    ("email", "password", "phone", "name", "message"),
    (
        ("", "", "", "", "Email not provided"),
        ("ebube@cortts.com", "", "", "", "Password not provided"),
        ("ebube@cortts.com", "something", "08162300796", "", "Name not provided"),
        ("ebube@cortts.com", "something", "", "Ebube", "Phone number not provided"),
        ("ebube@cortts.com", "something", "08162300796", "Ebube", "Email address already exist! try login"),
    ),
)
def test_register_validate_param(client, app, email, password, phone, name, message):
    data = dict(
        email=email,
        password=password,
        phone=phone,
        name=name
    )
    resp = client.post('/api/auth/create', json=data)
    json = resp.get_json()
    assert resp.status_code == 400

    assert json['status'] == 'error'
    assert message in json['msg']



def test_create_login(client, app):
    data = dict(
        email='ebubeidam@cortts.com',
        password='lilian01',
        phone='08162300796',
        name='Ebubechukwu'
    )
    res = client.post('/api/auth/create', json=data)
    assert res.status_code == 200
    json = res.get_json()

    assert json['status'] == 'success'
    assert 'token' in json
    assert 'refreshToken' in json 

    




    

    