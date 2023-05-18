import json
from app import create_app
from app.tests.utils import login

def test_uf():
    """Tests the uf route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    response = client.get('/uf', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'ufs' in keys
    assert type(body['success']['ufs']) is list

    keys = list(body['success']['ufs'][0].keys())

    assert 'uf' in keys

def test_uf_with_cities():
    """Tests the uf and cities route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    response = client.get('/uf-with-cities', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'ufs' in keys
    assert type(body['success']['ufs']) is list

    keys = list(body['success']['ufs'][0].keys())

    assert 'uf' in keys
    assert 'cities' in keys
    assert type(body['success']['ufs'][0]['cities']) is list

    keys = list(body['success']['ufs'][0]['cities'].keys())

    assert 'id' in keys
    assert 'city' in keys