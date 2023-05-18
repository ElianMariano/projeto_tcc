import json
from app import create_app
from app.tests.utils import login

def test_get_fono():
    """Tests the fono get route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    ID = 1 # Considers the first id

    response = client.get('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    # Asserts if key exists is changed
    assert 'id' in keys
    assert 'nome' in keys
    assert 'nascimento' in keys
    assert 'cpf' in keys
    assert 'endereco' in keys
    assert 'cidade_id' in keys
    assert 'nivel_id' in keys

def test_list_fono():
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
    assert 'nome' in keys
    assert 'nascimento' in keys
    assert 'cpf' in keys
    assert 'endereco' in keys
    assert 'cidade_id' in keys
    assert 'nivel_id' in keys

def test_create_fono():
    """Tests the fono creation route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999999', 'endereco': '', 'senha': 'senha123', 'cidade_id': 1, 'nivel_id': 1}

    response = client.post('/fono', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 201

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'nome' in keys
    assert 'nascimento' in keys
    assert 'cpf' in keys
    assert 'endereco' in keys
    assert 'cidade_id' in keys
    assert 'nivel_id' in keys

def test_update_fono():
    """Tests the fono update route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999999', 'endereco': '', 'cidade_id': 1, 'nivel_id': 1, 'senha': 'senha123'}

    ID = 1 # Considers the first id

    response = client.put('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 202

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    # Asserts if key exists is changed
    assert 'id' in keys and body['success']['id'] == ID
    assert 'nome' in keys and body['success']['nome'] == data['nome']
    assert 'nascimento' in keys and body['success']['nascimento'] == data['nascimento']
    assert 'cpf' in keys and body['success']['cpf'] == data['cpf']
    assert 'endereco' in keys and body['success']['endereco'] == data['endereco']
    assert 'cidade_id' in keys and body['success']['cidade_id'] == data['cidade_id']
    assert 'nivel_id' in keys and body['success']['nivel_id'] == data['nivel_id']

def test_delete_fono():
    """Tests the fono delete route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    response = client.delete('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})

    assert response.status_code == 202

def test_fono_date_format_error():
    """Tests the fono data format error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-', 'cpf': '99999999999', 'endereco': '', 'cidade_id': 1, 'nivel_id': 1, 'senha': 'senha123'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Formato de data inválida.'

def test_fono_cpf_format_error():
    """Tests the fono cpf format error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999', 'endereco': '', 'cidade_id': 1, 'nivel_id': 1, 'senha': 'senha123'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Formato de cpf inválida.'

def test_fono_no_city_error():
    """Tests the fono city does not exist error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999', 'endereco': '', 'cidade_id': 10, 'nivel_id': 1, 'senha': 'senha123'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Cidade não encontrada.'

def test_fono_no_level_error():
    """Tests the fono level does not exist error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999', 'endereco': '', 'cidade_id': 1, 'nivel_id': 10,  'senha': 'senha123'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Nível não encontrado.'

def test_fono_password_error():
    """Tests the fono password error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999', 'endereco': '', 'cidade_id': 1, 'nivel_id': 10,  'senha': 'senha'}

    response = client.post('/fono/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'A senha deve ser maior que 8 caracteres.'

def test_no_fono():
    """Tests no option"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 10 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999', 'endereco': '', 'cidade_id': 1, 'nivel_id': 10,  'senha': 'senha'}

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