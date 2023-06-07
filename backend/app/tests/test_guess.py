import json
from app import create_app
from app.tests.utils import login
from app import tests

def test_get_guess(session):
    """Tests the guess get route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    ID = 1 # Considers the first id

    response = client.get('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'pacient_id' in keys
    assert 'level_id' in keys
    assert 'right' in keys

def test_list_guess(session):
    """Tests the guess list route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    response = client.get('/guess', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert type(body['success']['guesses']) is list

    keys = list(body['success']['guesses'][0].keys())

    assert 'id' in keys
    assert 'pacient_id' in keys
    assert 'level_id' in keys
    assert 'right' in keys

def test_create_guess(session):
    """Tests the guess route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'pacient_id': 1, 'level_id': 1, 'right': True}

    response = client.post('/guess', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 201

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'pacient_id' in keys
    assert 'level_id' in keys
    assert 'right' in keys

def test_update_guess(session):
    """Tests the guess update route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'pacient_id': 1, 'level_id': 1, 'right': True}

    ID = 1 # Considers the first id

    response = client.put('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 202

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys and body['success']['id'] == ID
    assert 'pacient_id' in keys and body['success']['pacient_id'] == data['pacient_id']
    assert 'level_id' in keys and body['success']['level_id'] == data['level_id']
    assert 'right' in keys and body['success']['right'] == data['right']

def test_delete_guess(session):
    """Tests the guess delete route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    response = client.delete('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})

    assert response.status_code == 202

def test_guess_no_pacient_error(session):
    """Tests the guess does not have pacient error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'pacient_id': 10, 'level_id': 1, 'right': True}

    response = client.post('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Paciente não encontrado.'

def test_guess_no_level_error(session):
    """Tests the guess does not have level error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'pacient_id': 1, 'level_id': 10, 'right': True}

    response = client.post('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Nível não encontrado.'

def test_no_guess(session):
    """Tests no guess"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 10 # Considers the first id

    data = {'pacient_id': 1, 'level_id': 10, 'right': True}

    response = client.put('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Tentativa não encontrada.'

    response = client.delete('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Tentativa não encontrada.'