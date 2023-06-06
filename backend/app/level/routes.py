from flask import request, make_response, Response, jsonify
from app.level import blueprint
from app.level.models import *

@blueprint.get('/level/<int:id>')
def index(id):
    level = Nivel.query.get(id)

    return make_response(jsonify(level.as_dict()), 200)

@blueprint.get('/level')
def list():
    levels = Nivel.query.all()

    return make_response(jsonify(level.as_dict() for level in levels), 200)

@blueprint.post('/level')
def create():
    body = request.json

    level = Nivel(pontos=body['points'], dificuldade=body['difficulty'])
    
    db.session.add(level)
    db.session.commit()

    return make_response(jsonify(level.as_dict()), 200)

@blueprint.put('/level/<int:id>')
def update(id):
    body = request.json

    level = Nivel.query.get(id)
    level.pontos = body['points']
    level.dificuldade = body['difficulty']

    return make_response(jsonify(level.as_dict()), 200)

@blueprint.delete('/level/<int:id>')
def delete(id):
    level = Nivel.query.get(id)

    db.session.add(level)
    db.session.commit()

    return Response(status=202)