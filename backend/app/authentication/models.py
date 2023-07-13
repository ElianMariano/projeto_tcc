from app import db

class Fono(db.Model):
    __tablename__ = 'fono'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    senha = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, unique=True, nullable=False)
    endereco = db.Column(db.String, nullable=False)
    pacientes = db.relationship('Paciente', backref='fono') # , cascade='all, delete, delete-orphan'
    nivel_id = db.Column(db.Integer, db.ForeignKey('nivel.id'))

    def __init__(self, nome, nascimento, senha, cpf, endereco, email):
        self.nome = nome
        self.nascimento = nascimento
        self.senha = senha
        self.cpf = cpf
        self.endereco = endereco
        self.email = email
        # self.pacientes = pacientes

    def __repr__(self):
        return '<id {}, nome: {}, cpf: {}>'.format(self.id, self.nome, self.cpf)
    
    def as_dict(self):
        return {'id': self.id, 'name': self.nome, 'birth': self.nascimento, 'cpf': self.cpf, 'address': self.endereco, 'email': self.email}

class Paciente(db.Model):
    __tablename__ = 'paciente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    senha = db.Column(db.String, nullable=False)
    # cpf = db.Column(db.String, unique=True, nullable=False)
    pontos = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String, nullable=False)
    
    fono_id = db.Column(db.Integer, db.ForeignKey('fono.id'), nullable=False)
    guesses = db.relationship('Tentativa', backref='paciente')

    def __init__(self, nome, nascimento, senha, pontos, endereco, fono_id, email):
        self.nome = nome
        self.nascimento = nascimento
        self.senha = senha
        self.pontos = pontos
        self.endereco = endereco
        self.email = email
        self.fono_id

    def __repr__(self):
        return '<id {}, nome: {}>'.format(self.id, self.nome)

    def as_dict(self):
        return {'id': self.id, 'name': self.nome, 'birth': self.nascimento, 'address': self.endereco, 'fono_id': self.fono_id, 'points': self.pontos}