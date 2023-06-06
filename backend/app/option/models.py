from app import db

class Opcao(db.Model):
    __tablename__ = 'opcao'

    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String, nullable=False)
    correta = db.Column(db.Boolean, nullable=False)
    arquivo = db.Column(db.String, nullable=False)
    pergunta_id = db.Column(db.Integer, db.ForeignKey('pergunta.id'), nullable=False)

    def __init__(self, texto, correta, arquivo):
        self.texto = texto
        self.correta = correta
        self.arquivo = arquivo

    def __repr__(self):
        return '<id {}, texto: {}, correta: {}, arquivo: {}>'.format(self.id, self.texto, self.correta, self.arquivo)
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}