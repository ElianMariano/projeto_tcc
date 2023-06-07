from flask import request, make_response, Response, jsonify
from app.guess import blueprint
from app.guess.models import *
from app.errors.types import *
from app.level.models import *
from app.authentication.models import *
from app.authentication.utils import validate_params

@blueprint.get('/guess/<int:id>')
def index(id):
    guess = Tentativa.query.get(id)

    if guess == None:
        raise APIResourceNotFound('Tentativa não encontrada.')

    return make_response(jsonify({'success': guess.as_dict()}), 200)

@blueprint.get('/guess')
def list():
    guesses = Tentativa.query.all()

    return make_response(jsonify({'success': [guess.as_dict() for guess in guesses]}), 200)

@blueprint.post('/guess')
def create():
    body = request.json

    validate_params(['right', 'pacient_id', 'level_id'], body=body)

    level = Nivel.query.get(body['level_id'])

    if level == None:
        raise APIResourceNotFound('Nível não encontrado.')
    
    paciente = Paciente.query.get(body['level_id'])

    if paciente == None:
        raise APIResourceNotFound('Paciente não encontrado.')

    guess = Tentativa(correta=body['right'], paciente_id=body['pacient_id'], nivel_id=body['level_id'])

    db.session.add(guess)
    db.session.commit()

    return make_response(jsonify({'succcess': guess.as_dict()}), 200)

@blueprint.put('/guess/<int:id>')
def update(id):    
    body = request.json

    validate_params(['right', 'level_id'], body=body)

    guess = Tentativa.query.get(id)

    level = Nivel.query.get(body['level_id'])

    if level == None:
        raise APIResourceNotFound('Nível não encontrado.')

    if guess == None:
        raise APIResourceNotFound('Tentativa não encontrada.')

    guess.correta = body['right']
    guess.nivel_id = body['nivel_id']

    return make_response(jsonify({'success': guess.as_dict()}), 200)

@blueprint.delete('/guess/<int:id>')
def delete(id):
    guess = Tentativa.query.get(id)

    if guess == None:
        raise APIResourceNotFound('Tentativa não encontrada.')

    db.session.delete(guess)
    db.session.commit()

    return Response(status=202)