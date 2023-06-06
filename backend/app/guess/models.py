from app import db

class Tentativa(db.Model):
    __tablename__ = 'tentativa'

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    nivel_id = db.Column(db.Integer, db.ForeignKey('nivel.id'), nullable=False)
    correta = db.Column(db.Boolean, nullable=False)

    def __init__(self, correta, paciente_id, nivel_id):
        self.correta = correta
        self.paciente_id = paciente_id
        self.nivel_id = nivel_id

    def __repr__(self):
        return '<id {}, correta: {}=>'.format(self.id, self.correta)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}