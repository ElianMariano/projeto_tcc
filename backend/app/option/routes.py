from flask import request
from app.option import blueprint

@blueprint.get('/option/<int:id>')
def index(id):
    pass

@blueprint.get('/option')
def list():
    pass

@blueprint.post('/option')
def create():
    pass

@blueprint.put('/option/<int:id>')
def update(id):
    pass

@blueprint.delete('/option/<int:id>')
def delete(id):
    pass