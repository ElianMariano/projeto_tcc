from flask import Blueprint

blueprint = Blueprint(
    'errors',
    __name__,
    url_prefix=''
)