import pytest

from server.models.User import User


def test_create_login(client, app):
    data = dict(
        email='ebube@cortts.com',
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

    resp = client.post('/api/auth/login', json={'email': 'ebube@cortts.com', 'password': 'lilian01'})
    json = resp.get_json()
    assert resp.status_code == 200




    

    