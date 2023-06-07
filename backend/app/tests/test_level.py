import json
from app import create_app
from app.tests.utils import login
from app.tests import session

def test_get_level(session):
    """Tests the level get route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    ID = 1 # Considers the first id

    response = client.get('/level/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'points' in keys
    assert 'difficulty' in keys
    # assert 'nivel_numero' in keys

def test_list_level(session):
    """Tests the level list route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    response = client.get('/level', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert type(body['success']['levels']) is list

    keys = list(body['success']['levels'][0].keys())

    assert 'id' in keys
    assert 'points' in keys
    assert 'difficulty' in keys
    # assert 'nivel_numero' in keys

def test_create_level(session):
    """Tests the level route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'points': 10, 'difficulty': 'dificil', 'nivel_numero': 1}

    response = client.post('/level', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 201

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'points' in keys
    assert 'difficulty' in keys
    # assert 'nivel_numero' in keys

def test_update_level(session):
    """Tests the level update route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'points': 10, 'difficulty': 'dificil', 'nivel_numero': 1}

    ID = 1 # Considers the first id

    response = client.put('/level/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 202

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys and body['success']['id'] == ID
    assert 'points' in keys and body['success']['points'] == data['points']
    assert 'difficulty' in keys and body['success']['difficulty'] == data['difficulty']
    # assert 'nivel_numero' in keys and body['success']['nivel_numero'] == data['nivel_numero']

def test_delete_level(session):
    """Tests the level delete route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    response = client.delete('/level/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})

    assert response.status_code == 202

def test_no_level(session):
    """Tests no level"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 10 # Considers the first id

    data = {'points': 10, 'difficulty': 'dificil', 'nivel_numero': 1}

    response = client.put('/level/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Nível não encontrado.'

    response = client.delete('/level/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Nível não encontrado.'