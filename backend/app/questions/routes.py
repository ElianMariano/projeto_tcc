from flask import request
from app.questions import blueprint

@blueprint.get('/questions/<int:id>')
def index(id):
    pass

@blueprint.get('/questions')
def list():
    pass

@blueprint.post('/questions')
def create():
    pass

@blueprint.put('/questions/<int:id>')
def update(id):
    pass

@blueprint.delete('/questions/<int:id>')
def delete(id):
    pass