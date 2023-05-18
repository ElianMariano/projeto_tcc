import json
from app import create_app
from app.tests.utils import login

def test_get_pacient():
    """Tests the pacient get route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    ID = 1 # Considers the first id

    response = client.get('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'nome' in keys
    assert 'nascimento' in keys
    assert 'endereco' in keys
    assert 'pontos' in keys
    assert 'cidade_id' in keys
    assert 'fono_id' in keys

def test_list_pacient():
    """Tests the pacient list route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    response = client.get('/pacient', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert type(body['success']['pacients']) is list

    keys = list(body['success']['pacients'][0].keys())

    assert 'id' in keys
    assert 'nome' in keys
    assert 'nascimento' in keys
    assert 'endereco' in keys
    assert 'pontos' in keys
    assert 'cidade_id' in keys
    assert 'fono_id' in keys

def test_create_pacient():
    """Tests the pacient route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999999', 'endereco': '', 'senha': 'senha123', 'cidade_id': 1, 'fono_id': 1}

    response = client.post('/pacient', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 201

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'nome' in keys
    assert 'nascimento' in keys
    assert 'endereco' in keys
    assert 'pontos' in keys
    assert 'cidade_id' in keys
    assert 'fono_id' in keys

def test_update_pacient():
    """Tests the pacient update route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999999', 'endereco': '', 'senha': 'senha123', 'cidade_id': 1, 'fono_id': 1}

    ID = 1 # Considers the first id

    response = client.put('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 202

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys and body['success']['id'] == ID
    assert 'nome' in keys and body['success']['nome'] == data['nome']
    assert 'nascimento' in keys and body['success']['nascimento'] == data['nascimento']
    assert 'endereco' in keys and body['success']['endereco'] == data['endereco']
    assert 'pontos' in keys and body['success']['pontos'] == data['pontos']
    assert 'cidade_id' in keys
    assert 'fono_id' in keys
    assert 'fono_id' in keys and body['success']['fono_id'] == data['fono_id']

def test_delete_pacient():
    """Tests the pacient delete route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    response = client.delete('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})

    assert response.status_code == 202

def test_pacient_date_format_error():
    """Tests the pacient data format error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-2', 'cpf': '99999999999', 'endereco': '', 'senha': 'senha123', 'cidade_id': 1, 'fono_id': 1}

    response = client.post('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Formato de data inválida.'

def test_pacient_no_city_error():
    """Tests the pacient city does not exist error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999999', 'endereco': '', 'senha': 'senha123', 'cidade_id': 10, 'fono_id': 1}

    response = client.post('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Cidade não encontrada.'

def test_pacient_cpf_format_error():
    """Tests the pacient cpf format error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '999999', 'endereco': '', 'senha': 'senha123', 'cidade_id': 1, 'fono_id': 1}

    response = client.post('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Formato de cpf inválido.'

def test_pacient_no_fono_error():
    """Tests the pacient fono does not exist error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999999', 'endereco': '', 'senha': 'senha123', 'cidade_id': 1, 'fono_id': 10}

    response = client.post('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Fonoaudiólogo não encontrado.'

def test_pacient_password_error():
    """Tests the pacient password error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999999', 'endereco': '', 'senha': 'senha', 'cidade_id': 1, 'fono_id': 1}

    response = client.post('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'A senha deve ser maior que 8 caracteres.'

def test_no_pacient():
    """Tests no pacient"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 10 # Considers the first id

    data = {'nome': 'fono', 'nascimento': '1990-03-28', 'cpf': '99999999999', 'endereco': '', 'senha': 'senha', 'cidade_id': 1, 'fono_id': 1}

    response = client.put('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Paciente não encontrada.'

    response = client.delete('/pacient/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Opção não encontrada.'