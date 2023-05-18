import os
import json
from dotenv import dotenv_values
from app.authentication import blueprint
from flask import jsonify, make_response, request

@blueprint.route('/login', methods=['POST'])
def login():
    API_KEY = dotenv_values(os.path.join('.env'))['API_KEY']
    
    if ('x-api-key' in request.headers and request.headers['x-api-key'] != API_KEY):
        response = make_response(jsonify(error=401, message='API KEY inválida.'), 401)
        return response
    elif ('x-api-key' not in request.headers):
        response = make_response(jsonify(error=401, message='Nenhuma API KEY foi informada.'), 401)
        return response

    body = request.json

    if ('email' not in body):
        response = make_response(jsonify(error=400, message='Informe o email.'), 400)
        return response
    
    if ('senha' not in body):
        response = make_response(jsonify(error=400, message='Informe a senha.'), 400)
        return response
    
    # TODO CHECK PASSWORD

    response = make_response(jsonify(user='elian', token='token'), 200)
    return response