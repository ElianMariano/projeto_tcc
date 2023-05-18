import importlib
from flask import Flask
from app.authentication.routes import blueprint

MODULES = ('authentication',)

def register_modules(app):
    for module_name in MODULES:
        module = importlib.import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app():
    app = Flask(__name__)
    register_modules(app)
    return app