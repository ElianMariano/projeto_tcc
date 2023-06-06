import os
import json
from dotenv import dotenv_values
from app.authentication import blueprint
from flask import jsonify, make_response, request, Response
from app.authentication.models import *

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

# ============== Fono ==============

@blueprint.get('/fono/<int:id>')
def findex(id):
    fono = Fono.query.get(id)

    return make_response(jsonify(fono.as_dict()), 200)

@blueprint.get('/fono')
def flist():
    fonos = Fono.query.all()
    
    return make_response(jsonify([fono.as_dict() for fono in fonos]), 200)

@blueprint.post('/fono')
def fcreate():
    body = request.json

    fono = Fono(nome=body['name'], nascimento=body['birth'], senha=body['password'], cpf=body['cpf'], endereco=body['endereco'])

    db.session.add(fono)
    db.session.commit()

    return make_response(jsonify(body), 200)

@blueprint.put('/fono/<int:id>')
def fupdate(id):
    fono = Fono.query.get(id)

    body = request.json

    fono.nome = body['name']
    fono.nascimento = body['birth']
    fono.senha = body['password']
    fono.cpf = body['cpf']
    fono.endereco = body['address']

    # db.session.update(fono)
    db.session.commit()

    return make_response(jsonify(fono.as_dict()), 200)

@blueprint.delete('/fono/<int:id>')
def fdelete(id):
    fono = Fono.query.get(id)

    db.session.delete(fono)
    db.session.commit()

    return Response(status=202)

# ============== Paciente ==============

@blueprint.get('/pacient/<int:id>')
def pindex(id):
    paciente = Paciente.query.get(id)

    return make_response(jsonify(paciente.as_dict()), 200)

@blueprint.get('/pacient')
def plist():
    pacientes = Paciente.query.all()
    
    return make_response(jsonify([paciente.as_dict() for paciente in pacientes]), 200)

@blueprint.post('/pacient')
def pcreate():
    body = request.json

    paciente = Paciente(nome=body['name'], nascimento=body['birth'], senha=body['password'], endereco=body['address'], pontos=0, fono_id=body['fono_id'])

    db.session.add(paciente)
    db.session.commit()

    return make_response(jsonify(body), 200)

@blueprint.put('/pacient/<int:id>')
def pupdate(id):
    paciente = Paciente.query.get(id)

    body = request.json

    paciente.nome = body['name']
    paciente.nascimento = body['birth']
    paciente.senha = body['password']
    paciente.endereco = body['address']

    # db.session.update(fono)
    db.session.commit()

    return make_response(jsonify(paciente.as_dict()), 200)

@blueprint.delete('/pacient/<int:id>')
def pdelete(id):
    paciente = Paciente.query.get(id)

    db.session.delete(paciente)
    db.session.commit()

    return Response(status=202)