from database import db

class Reserva(db.Model):
    __tablename__ = 'reserva'
    id = db.Column(db.Integer, primary_key=True)
    num_sala = db.Column(db.String(20), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)