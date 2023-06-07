from flask import request, make_response, Response, jsonify
from app.level import blueprint
from app.level.models import *
from app.errors.types import *
from app.authentication.utils import validate_params

@blueprint.get('/level/<int:id>')
def index(id):
    level = Nivel.query.get(id)

    if level == None:
        raise APIResourceNotFound('Nível não encontrado.')

    return make_response(jsonify({'success': level.as_dict()}), 200)

@blueprint.get('/level')
def list():
    levels = Nivel.query.all()

    return make_response(jsonify({'success': [level.as_dict() for level in levels]}), 200)

@blueprint.post('/level')
def create():
    body = request.json

    validate_params(['points', 'difficulty'], body=body)

    level = Nivel(pontos=body['points'], dificuldade=body['difficulty'])
    
    db.session.add(level)
    db.session.commit()

    return make_response(jsonify({'success': level.as_dict()}), 200)

@blueprint.put('/level/<int:id>')
def update(id):
    body = request.json

    validate_params(['points', 'difficulty'], body=body)

    level = Nivel.query.get(id)

    if level == None:
        raise APIResourceNotFound('Nível não encontrado.')

    level.pontos = body['points']
    level.dificuldade = body['difficulty']

    return make_response(jsonify({'success': level.as_dict()}), 200)

@blueprint.delete('/level/<int:id>')
def delete(id):
    level = Nivel.query.get(id)

    if level == None:
        raise APIResourceNotFound('Nível não encontrado.')

    db.session.delete(level)
    db.session.commit()

    return Response(status=202)