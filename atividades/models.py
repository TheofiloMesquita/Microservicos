from database import db

class Atividade(db.Model):
    __tablename__ = 'atividade'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    peso = db.Column(db.Float, nullable=False)
    prazo = db.Column(db.String(20), nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)

class Nota(db.Model):
    __tablename__ = 'nota'
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    aluno_id = db.Column(db.Integer, nullable=False)
    atividade_id = db.Column(db.Integer, db.ForeignKey('atividade.id'))