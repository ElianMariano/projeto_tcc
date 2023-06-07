import pytest
from app.authentication.models import *
from app.guess.models import *
from app.level.models import *
from app.option.models import *
from app.questions.models import *
from app import create_app, db

@pytest.fixture
def session():
    app = create_app()
    
    with app.app_context():
        Fono.query.delete()
        # Paciente.query.delete()
        # Nivel.query.delete()
        # Pergunta.query.delete()
        # Opcao.query.delete()

    yield db