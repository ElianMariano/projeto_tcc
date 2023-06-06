from flask import request, make_response, Response, jsonify
from app.guess import blueprint
from app.guess.models import *

@blueprint.get('/guess/<int:id>')
def index(id):
    guess = Tentativa.query.get(id)

    return make_response(jsonify(guess.as_dict()), 200)

@blueprint.get('/guess')
def list():
    guesses = Tentativa.query.all()

    return make_response(jsonify(guess.as_dict() for guess in guesses), 200)

@blueprint.post('/guess')
def create():
    body = request.json

    guess = Tentativa(correta=body['right'], paciente_id=body['paciente_id'], nivel_id=body['nivel_id'])

    db.session.add(guess)
    db.session.commit()

    return make_response(jsonify(guess.as_dict()), 200)

@blueprint.put('/guess/<int:id>')
def update(id):
    body = request.json

    guess = Tentativa.query.get(id)
    guess.correta = body['right']
    guess.nivel_id = body['nivel_id']

    return make_response(jsonify(guess.as_dict()), 200)

@blueprint.delete('/guess/<int:id>')
def delete(id):
    guess = Tentativa.query.get(id)

    db.session.delete(guess)
    db.session.commit()

    return Response(status=202)