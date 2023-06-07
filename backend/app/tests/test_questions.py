import json
from app import create_app
from app.tests.utils import login
from app.tests import session

def test_get_questions(session):
    """Tests the questions get route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    ID = 1 # Considers the first id

    response = client.get('/questions/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'text' in keys
    assert 'level_id' in keys

def test_list_questions(session):
    """Tests the questions list route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    response = client.get('/questions', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 200

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert type(body['success']['questions']) is list

    keys = list(body['success']['questions'][0].keys())

    assert 'id' in keys
    assert 'text' in keys
    assert 'level_id' in keys

def test_create_questions(session):
    """Tests the questions route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'text': 'text', 'level_id': 1}

    response = client.post('/questions', headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 201

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys
    assert 'text' in keys
    assert 'level_id' in keys

def test_update_questions(session):
    """Tests the questions update route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)

    data = {'text': 'text', 'level_id': 1}

    ID = 1 # Considers the first id

    response = client.put('/questions/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 202

    keys = list(body.keys())

    assert 'success' in keys

    keys = list(body['success'].keys())

    assert 'id' in keys and body['success']['id'] == ID
    assert 'text' in keys and body['success']['text'] == data['text']
    assert 'level_id' in keys and body['success']['level_id'] == data['level_id']

def test_delete_questions(session):
    """Tests the questions delete route"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    response = client.delete('/questions/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'})

    assert response.status_code == 202

def test_question_no_level_error(session):
    """Tests the question does not have level error"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 1 # Considers the first id

    data = {'text': 'text', 'level_id': 10}

    response = client.post('/questions/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Nível não encontrado.'

def test_no_questions(session):
    """Tests no questions"""
    client = create_app().test_client()

    (TOKEN, API_KEY) = login(client)
    ID = 10 # Considers the first id

    data = {'text': 'text', 'level_id': 10}

    response = client.put('/questions/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Questão não encontrada.'

    response = client.delete('/questions/{}'.format(ID), headers={'Authorization:': 'Bearer {}'.format(TOKEN), 'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps(data))
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Questão não encontrada.'