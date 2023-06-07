from flask import request, jsonify, Response, make_response
from app.option import blueprint
from app.option.models import *
from app.errors.types import *
from app.authentication.utils import validate_params

@blueprint.get('/option/<int:id>')
def index(id):
    opcao = Opcao.query.get(id)

    if opcao == None:
        raise APIResourceNotFound('Opção não encontrada.')

    return make_response(jsonify({'success': opcao.as_dict()}), 200)

@blueprint.get('/option')
def list():
    opcoes = Opcao.query.all()

    return make_response(jsonify({'success': [opcao.as_dict for opcao in opcoes]}), 200)

@blueprint.post('/option')
def create():
    body = request.json

    validate_params('text', 'right', body=body)

    opcao = Opcao(texto=body['text'], correta=body['right'], arquivo=body['file'])

    db.session.add(opcao)
    db.session.commit()

    return make_response(jsonify({'success': opcao.as_dict()}), 201)

@blueprint.put('/option/<int:id>')
def update(id):
    body = request.json

    validate_params('text', 'right', body=body)

    opcao = Opcao.query.get(id)

    if opcao == None:
        raise APIResourceNotFound('Opção não encontrada.')

    opcao.texto = body['text']
    opcao.correta = body['right']

    return make_response(jsonify({'success': opcao.as_dict()}), 202)

@blueprint.delete('/option/<int:id>')
def delete(id):
    opcao = Opcao.query.get(id)

    if opcao == None:
        raise APIResourceNotFound('Opção não encontrada.')

    db.session.delete(opcao)
    db.session.commit()

    return Response(status=202)