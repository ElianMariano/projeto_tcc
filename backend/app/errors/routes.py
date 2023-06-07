from flask import request, jsonify, make_response, Response
from app.errors import blueprint
from app.errors.types import *

@blueprint.errorhandler(APINotFound)
@blueprint.errorhandler(APIResourceNotFound)
@blueprint.errorhandler(APIMissingParams)
@blueprint.errorhandler(APIAuthError)
def error(err):
    return make_response(jsonify(err.as_dict()), err.error)

@blueprint.errorhandler(500)
def default(err):
    return make_response(jsonify({'error': 500, 'message': 'Erro interno do servidor.'}), 500)