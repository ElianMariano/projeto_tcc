import json
from app.tests import session
from app import create_app
from app.tests.utils import login
from app.authentication.models import *
from app import db

def test_get_fono(session):
    """Tests the fono get route"""
    client = create_app().test_client()

    # (TOKEN, API_KEY) = login(client)

    ID = 1 # Considers the first id

    response = client.get('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    # Asserts if key exists is changed
    assert 'id' in keys
    assert 'name' in keys
    assert 'birth' in keys
    assert 'cpf' in keys
    assert 'address' in keys
    # assert 'cidade_id' in keys
    assert 'level_id' in keys

def test_list_fono(session):
    """Tests the fono list route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    response = client.get('/fono', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert type(body['success']['fono']) is list

    keys = list(body['success']['fono'][0].keys())

    assert 'id' in keys
    assert 'name' in keys
    assert 'birth' in keys
    assert 'cpf' in keys
    assert 'address' in keys
    # assert 'cidade_id' in keys
    assert 'level_id' in keys

def test_create_fono(session):
    """Tests the fono creation route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'name': 'fono', 'birth': '1990-03-28', 'cpf': '99999999999', 'address': '', 'senha': 'senha123', 'cidade_id': 1, 'level_id': 1}

    response = client.post('/fono', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 201

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'name' in keys
    assert 'birth' in keys
    assert 'cpf' in keys
    assert 'address' in keys
    # assert 'cidade_id' in keys
    assert 'level_id' in keys

def test_update_fono(session):
    """Tests the fono update route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'name': 'fono', 'birth': '1990-03-28', 'cpf': '99999999999', 'address': '', 'cidade_id': 1, 'level_id': 1, 'senha': 'senha123'}

    ID = 1 # Considers the first id

    response = client.put('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 202

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    # Asserts if key exists is changed
    assert 'id' in keys and body['success']['id'] == ID
    assert 'name' in keys and body['success']['name'] == data['name']
    assert 'birth' in keys and body['success']['birth'] == data['birth']
    assert 'cpf' in keys and body['success']['cpf'] == data['cpf']
    assert 'address' in keys and body['success']['address'] == data['address']
    # assert 'cidade_id' in keys and body['success']['cidade_id'] == data['cidade_id']
    assert 'level_id' in keys and body['success']['level_id'] == data['level_id']

def test_delete_fono(session):
    """Tests the fono delete route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    response = client.delete('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})

    assert response.status_code == 202

def test_fono_date_format_error(session):
    """Tests the fono data format error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'name': 'fono', 'birth': '1990-03-', 'cpf': '99999999999', 'address': '', 'cidade_id': 1, 'level_id': 1, 'senha': 'senha123'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Formato de data inválida.'

def test_fono_cpf_format_error(session):
    """Tests the fono cpf format error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'name': 'fono', 'birth': '1990-03-28', 'cpf': '99999999', 'address': '', 'cidade_id': 1, 'level_id': 1, 'senha': 'senha123'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Formato de cpf inválida.'

def test_fono_no_city_error(session):
    """Tests the fono city does not exist error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'name': 'fono', 'birth': '1990-03-28', 'cpf': '99999999', 'address': '', 'cidade_id': 10, 'level_id': 1, 'senha': 'senha123'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Cidade não encontrada.'

def test_fono_no_level_error(session):
    """Tests the fono level does not exist error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'name': 'fono', 'birth': '1990-03-28', 'cpf': '99999999', 'address': '', 'cidade_id': 1, 'level_id': 10,  'senha': 'senha123'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Nível não encontrado.'

def test_fono_password_error(session):
    """Tests the fono password error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'name': 'fono', 'birth': '1990-03-28', 'cpf': '99999999', 'address': '', 'cidade_id': 1, 'level_id': 10,  'senha': 'senha'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'A senha deve ser maior que 8 caracteres.'

def test_no_fono(session):
    """Tests no option"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 10 # Considers the first id

    data = {'name': 'fono', 'birth': '1990-03-28', 'cpf': '99999999', 'address': '', 'cidade_id': 1, 'level_id': 10,  'senha': 'senha'}

    response = client.put('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Fonoaudiólogo não encontrado.'

    response = client.delete('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Fonoaudiólogo não encontrado.'