from flask import request, Response, make_response, jsonify
from app.questions import blueprint
from app.questions.models import *
from app.errors.types import *
from app.level.models import *
from app.authentication.utils import validate_params

@blueprint.get('/questions/<int:id>')
def index(id):
    pergunta = Pergunta.query.get(id)

    if pergunta == None:
        raise APIResourceNotFound('Questão não encontrada.')

    return make_response(jsonify({'success': pergunta.as_dict()}), 200)

@blueprint.get('/questions')
def list():
    perguntas = Pergunta.query.all()

    return make_response(jsonify({'success': [pergunta.as_dict() for pergunta in perguntas]}), 200)

@blueprint.post('/questions')
def create():
    body = request.json

    validate_params(['text', 'level_id'], body=body)

    level = Nivel.query.get(body['level_id'])

    if level == None:
        raise APIResourceNotFound('Nível não encontrado.')

    pergunta = Pergunta(texto=body['text'], nivel_id=body['level_id'])

    db.session.add(pergunta)
    db.session.commit()

    return make_response(jsonify({'success': pergunta.as_dict()}), 201)

@blueprint.put('/questions/<int:id>')
def update(id):
    body = request.json

    validate_params(['text', 'level_id'], body=body)

    level = Nivel.query.get(body['level_id'])    

    pergunta = Pergunta.query.get(id)

    if level == None:
        raise APIResourceNotFound('Nível não encontrado.')

    if pergunta == None:
        raise APIResourceNotFound('Questão não encontrada.')

    pergunta.texto = body['text']
    pergunta.nivel_id = body['level_id']

    return make_response(jsonify({'success': pergunta.as_dict()}), 202)

@blueprint.delete('/questions/<int:id>')
def delete(id):
    pergunta = Pergunta.query.get(id)

    if pergunta == None:
        raise APIResourceNotFound('Questão não encontrada.')

    db.session.delete(pergunta)
    db.session.commit()

    return make_response(jsonify(pergunta.as_dict()), 202)