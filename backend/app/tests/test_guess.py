import json
from app import create_app
from app.tests.utils import login

def test_get_guess():
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
    assert 'paciente_id' in keys
    assert 'nivel_id' in keys
    assert 'correto' in keys

def test_list_guess():
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
    assert 'paciente_id' in keys
    assert 'nivel_id' in keys
    assert 'correto' in keys

def test_create_guess():
    """Tests the guess route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'paciente_id': 1, 'nivel_id': 1, 'correto': True}

    response = client.post('/guess', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 201

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'paciente_id' in keys
    assert 'nivel_id' in keys
    assert 'correto' in keys

def test_update_guess():
    """Tests the guess update route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'paciente_id': 1, 'nivel_id': 1, 'correto': True}

    ID = 1 # Considers the first id

    response = client.put('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 202

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys and body['success']['id'] == ID
    assert 'paciente_id' in keys and body['success']['paciente_id'] == data['paciente_id']
    assert 'nivel_id' in keys and body['success']['nivel_id'] == data['nivel_id']
    assert 'correto' in keys and body['success']['correto'] == data['correto']

def test_delete_guess():
    """Tests the guess delete route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    response = client.delete('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})

    assert response.status_code == 202

def test_guess_no_pacient_error():
    """Tests the guess does not have pacient error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'paciente_id': 10, 'nivel_id': 1, 'correto': True}

    response = client.post('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Paciente não encontrado.'

def test_guess_no_level_error():
    """Tests the guess does not have level error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'paciente_id': 1, 'nivel_id': 10, 'correto': True}

    response = client.post('/guess/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Nível não encontrado.'

def test_no_guess():
    """Tests no guess"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 10 # Considers the first id

    data = {'paciente_id': 1, 'nivel_id': 10, 'correto': True}

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