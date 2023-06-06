from app import db

class Pergunta(db.Model):
    __tablename__ = 'pergunta'

    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String, nullable=False)
    nivel_id = db.Column(db.Integer, db.ForeignKey('nivel.id'), nullable=False)

    options = db.relationship('Opcao', backref='pergunta')

    def __init__(self, texto):
        self.texto = texto

    def __repr__(self):
        return '<id {}, texto: {}=>'.format(self.id, self.texto)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}