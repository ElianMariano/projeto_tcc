from flask import Blueprint

blueprint = Blueprint(
    'guess',
    __name__,
    url_prefix=''
)