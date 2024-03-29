import os
import json
from dotenv import dotenv_values
from app.authentication import blueprint
from flask import jsonify, make_response, request, Response, send_from_directory
from app.authentication.models import *
from app.errors.types import *
from app.authentication.utils import validate_params

@blueprint.route('/static/<path>')
def static(path):
    return send_from_directory('assets', path)

@blueprint.route('/login', methods=['POST'])
def login():
    API_KEY = dotenv_values(os.path.join('.env'))['API_KEY']
    
    # if ('x-api-key' in request.headers and request.headers['x-api-key'] != API_KEY):
    #     response = make_response(jsonify(error=401, message='API KEY inválida.'), 401)
    #     return response
    # elif ('x-api-key' not in request.headers):
    #     response = make_response(jsonify(error=401, message='Nenhuma API KEY foi informada.'), 401)
    #     return response

    body = request.json

    if ('email' not in body):
        response = make_response(jsonify(error=400, message='Informe o email.'), 400)
        return response
    
    if ('senha' not in body):
        response = make_response(jsonify(error=400, message='Informe a senha.'), 400)
        return response
    
    # TODO CHECK PASSWORD

    fono = list(Fono.query.filter(Fono.email == body['email']).filter(Fono.senha == body['senha']))

    paciente = list(Paciente.query.filter(Paciente.email == body['email']).filter(Paciente.senha == body['senha']))

    if len(fono) > 0:
        response = make_response(jsonify({'success': fono[0].as_dict()}), 200)
        return response
    
    if (len(paciente)) > 0:
        response = make_response(jsonify({'success': fono[0].as_dict()}), 200)
        return response

    response = make_response(jsonify({'error': 'Usuário não encontrado.', 'code': 400}), 400)
    return response

# ============== Fono ==============

@blueprint.get('/fono/<int:id>')
def findex(id):
    fono = Fono.query.get(id)

    if fono == None:
        raise APINotFound('Fonoaudiólogo não encontrado.')

    return make_response(jsonify({'success': fono.as_dict()}), 200)

@blueprint.get('/fono')
def flist():
    fonos = Fono.query.all()
    
    return make_response(jsonify({'success': [fono.as_dict() for fono in fonos]}), 200)

@blueprint.post('/fono')
def fcreate():
    body = request.json

    validate_params(['name', 'birth', 'password', 'cpf', 'address', 'email'], body=body)

    fono = Fono(nome=body['name'], nascimento=body['birth'], senha=body['password'], cpf=body['cpf'], endereco=body['address'], email=body['email'])

    db.session.add(fono)
    db.session.commit()

    return make_response(jsonify({'success': fono.as_dict()}), 200)

@blueprint.put('/fono/<int:id>')
def fupdate(id):
    fono = Fono.query.get(id)

    if fono == None:
        raise APINotFound('Fonoaudiólogo não encontrado.')

    body = request.json
    
    validate_params(['name', 'birth', 'password', 'cpf', 'address', 'email'], body=body)

    fono.nome = body['name']
    fono.nascimento = body['birth']
    fono.email = body['email']
    fono.senha = body['password']
    fono.cpf = body['cpf']
    fono.endereco = body['address']

    # db.session.update(fono)
    db.session.commit()

    return make_response(jsonify({'success': fono.as_dict()}), 200)

@blueprint.delete('/fono/<int:id>')
def fdelete(id):
    fono = Fono.query.get(id)

    if fono == None:
        raise APINotFound('Fonoaudiólogo não encontrado.')

    db.session.delete(fono)
    db.session.commit()

    return Response(status=202)

# ============== Paciente ==============

@blueprint.get('/pacient/<int:id>')
def pindex(id):
    paciente = Paciente.query.get(id)

    if paciente == None:
        raise APINotFound('Paciente não encontrado.')

    return make_response(jsonify({'success': paciente.as_dict()}), 200)

@blueprint.get('/pacient')
def plist():
    pacientes = Paciente.query.all()
    
    return make_response(jsonify({'success': [paciente.as_dict() for paciente in pacientes]}), 200)

@blueprint.post('/pacient')
def pcreate():
    body = request.json

    validate_params(['name', 'birth', 'password', 'fono_id', 'address', 'email'], body=body)

    fono = Fono.query.get(body['fono_id'])
    
    if fono == None:
        raise APINotFound('Fonoaudiólogo não encontrado.')

    paciente = Paciente(nome=body['name'], nascimento=body['birth'], senha=body['password'], endereco=body['address'], pontos=0, fono_id=body['fono_id'], email=body['email'])

    db.session.add(paciente)
    db.session.commit()

    return make_response(jsonify({'success': paciente.as_dict()}), 200)

@blueprint.put('/pacient/<int:id>')
def pupdate(id):
    paciente = Paciente.query.get(id)

    if paciente == None:
        raise APINotFound('Paciente não encontrado.')

    body = request.json

    validate_params(['name', 'birth', 'password', 'fono_id', 'address', 'email'], body=body)

    fono = Fono.query.get(body['fono_id'])
    
    if fono == None:
        raise APINotFound('Fonoaudiólogo não encontrado.')

    paciente.nome = body['name']
    paciente.nascimento = body['birth']
    paciente.senha = body['password']
    paciente.endereco = body['address']
    paciente.email = body['email']

    # db.session.update(fono)
    db.session.commit()

    return make_response(jsonify({'success': paciente.as_dict()}), 200)

@blueprint.delete('/pacient/<int:id>')
def pdelete(id):
    paciente = Paciente.query.get(id)

    if paciente == None:
        raise APINotFound('Paciente não encontrado.')

    db.session.delete(paciente)
    db.session.commit()

    return Response(status=202)