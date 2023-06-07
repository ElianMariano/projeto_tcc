import json
from app import create_app
from app.tests.utils import login
from app.tests import session

def test_get_option(session):
    """Tests the option get route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    ID = 1 # Considers the first id

    response = client.get('/option/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'right' in keys
    assert 'file' in keys
    # assert 'pergunta_id' in keys


def test_list_option(session):
    """Tests the option list route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    response = client.get('/option', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert type(body['success']['options']) is list

    keys = list(body['success']['options'][0].keys())

    assert 'id' in keys
    assert 'right' in keys
    assert 'file' in keys
    # assert 'pergunta_id' in keys

def test_create_option(session):
    """Tests the option route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'right': True, 'file': 'file.mp3', 'nivel_id': 1}

    response = client.post('/option', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 201

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'right' in keys
    assert 'file' in keys
    # assert 'pergunta_id' in keys

def test_update_option(session):
    """Tests the option update route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'right': True, 'file': 'file.mp3', 'nivel_id': 1}

    ID = 1 # Considers the first id

    response = client.put('/option/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 202

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys and body['success']['id'] == ID
    assert 'right' in keys and body['success']['right'] == data['right']
    assert 'file' in keys and body['success']['file'] == data['file']
    # assert 'pergunta_id' in keys and body['success']['pergunta_id'] == data['pergunta_id']

def test_delete_option(session):
    """Tests the option delete route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    response = client.delete('/option/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})

    assert response.status_code == 202

def test_option_no_question_error(session):
    """Tests the option does not have question error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'texto': 'texto', 'right': True, 'file': 'file.mp3', 'pergunta_id': 10}

    response = client.post('/option/', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Pergunta não encontrada.'

def test_no_option(session):
    """Tests no option"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 10 # Considers the first id

    data = {'texto': 'texto', 'right': True, 'file': 'file.mp3', 'pergunta_id': 10}

    response = client.put('/option/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Opção não encontrada.'

    response = client.delete('/option/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Opção não encontrada.'