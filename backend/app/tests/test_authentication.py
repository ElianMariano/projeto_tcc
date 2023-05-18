import json
import os
from app import create_app
from dotenv import dotenv_values

def test_login():
    """Tests the login route"""
    client = create_app().test_client()

    API_KEY = dotenv_values('.env')['API_KEY']

    response = client.post('/login', headers={'x_api_key': API_KEY, 'Content-Type': 'application/json'}, data=json.dumps({'email': 'email@gmail.com', 'senha': 'senha'}))
    body = response.json

    assert response.status_code == 200
    
    keys = list(body.keys())

    assert 'user' in keys
    assert 'token' in keys

def test_password():
    """Tests login password"""
    client = create_app().test_client()

    API_KEY = dotenv_values('.env')['API_KEY']

    response = client.post('/login', data=json.dumps({'email': 'email@gmail.com', 'senha': 'senha2'}), headers={'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 401

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 401
    assert body['message'] == 'Usuário/Senha inválidos.'

def test_missing_email():
    """Tests missing email"""
    client = create_app().test_client()

    API_KEY = dotenv_values('.env')['API_KEY']

    response = client.post('/login', data=json.dumps({'senha': 'senha'}), headers={'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Informe o email.'

def test_missing_password():
    """Tests missing password"""
    client = create_app().test_client()

    API_KEY = dotenv_values('.env')['API_KEY']

    response = client.post('/login', data=json.dumps({'email': 'email@gmail.com'}), headers={'x_api_key': API_KEY, 'Content-Type': 'application/json'})
    body = response.json

    assert response.status_code == 400

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 400
    assert body['message'] == 'Informe a senha.'

def test_no_api():
    """Tests no api key"""
    client = create_app().test_client()

    response = client.post('/login', headers={'Content-Type': 'application/json'}, data=json.dumps({'email': 'email@gmail.com', 'senha': 'senha'}))
    body = response.json

    assert response.status_code == 401

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 401
    assert body['message'] == 'Nenhuma API KEY foi informada.'

def test_invalid_api():
    """Tests invalid api key"""
    client = create_app().test_client()

    response = client.post('/login', headers={'x_api_key': 'abs', 'Content-Type': 'application/json'}, data=json.dumps({'email': 'email@gmail.com', 'senha': 'senha'}))
    body = response.json

    assert response.status_code == 401

    keys = list(body.keys())

    assert 'error' in keys
    assert 'message' in keys
    assert body['error'] == 401
    assert body['message'] == 'API KEY inválida.'