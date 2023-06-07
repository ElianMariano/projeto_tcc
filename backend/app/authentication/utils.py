from app.errors.types import *

def validate_params(params, body):
    missing = []

    for element in params:
        if element not in body:
            missing.append(element)
    
    if len(missing) != 0:
        raise APIMissingParams("Por favor, envie os seguintes parâmetros: {}\n".format(', '.join(missing)))