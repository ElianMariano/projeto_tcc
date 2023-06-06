from app import db

class Nivel(db.Model):
    __tablename__ = 'nivel'

    id = db.Column(db.Integer, primary_key=True)
    pontos = db.Column(db.Integer, nullable=False)
    dificuldade = db.Column(db.String, nullable=False)

    fonos = db.relationship('Fono', backref='nivel')
    guess = db.relationship('Tentativa', backref='nivel')
    questions = db.relationship('Pergunta', backref='nivel')

    def __init__(self, pontos, dificuldade):
        self.pontos = pontos
        self.dificuldade = dificuldade

    def __repr__(self):
        return '<id {}, pontos: {}, dificuldade: {}>'.format(self.id, self.pontos, self.dificuldade)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}