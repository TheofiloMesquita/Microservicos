from flask import jsonify, request
from models import db, Reserva
import requests

GERENCIAMENTO_URL = "http://gerenciamento:5001"

def get_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {"id": r.id, "num_sala": r.num_sala, "data": r.data, "turma_id": r.turma_id}
        for r in reservas
    ])

def create_reserva():
    data = request.json
    turma_id = data.get("turma_id")

    # Verifica se a turma existe no serviço de gerenciamento
    try:
        resp = requests.get(f"{GERENCIAMENTO_URL}/turmas")
        turmas = resp.json()
        if not any(t["id"] == turma_id for t in turmas):
            return jsonify({"error": "Turma inexistente"}), 400
    except Exception as e:
        return jsonify({"error": "Erro ao comunicar com serviço de gerenciamento", "details": str(e)}), 500

    reserva = Reserva(num_sala=data["num_sala"], data=data["data"], turma_id=turma_id)
    db.session.add(reserva)
    db.session.commit()
    return jsonify({"message": "Reserva criada", "id": reserva.id}), 201

def update_reserva(id):
    data = request.json
    reserva = Reserva.query.get_or_404(id)
    reserva.num_sala = data.get("num_sala", reserva.num_sala)
    reserva.data = data.get("data", reserva.data)
    db.session.commit()
    return jsonify({"message": "Reserva atualizada"})

def delete_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify({"message": "Reserva removida"})