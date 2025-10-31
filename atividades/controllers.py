from flask import jsonify, request
from models import db, Atividade, Nota
import requests

GERENCIAMENTO_URL = "http://gerenciamento:5001"

# ------------------------------
# CRUD Atividades
# ------------------------------
def get_atividades():
    atividades = Atividade.query.all()
    return jsonify([
        {
            "id": a.id,
            "descricao": a.descricao,
            "peso": a.peso,
            "prazo": a.prazo,
            "turma_id": a.turma_id,
            "professor_id": a.professor_id
        } for a in atividades
    ])

def create_atividade():
    data = request.json
    turma_id = data.get("turma_id")
    professor_id = data.get("professor_id")

    # Verifica se turma e professor existem no serviço de gerenciamento
    try:
        t_resp = requests.get(f"{GERENCIAMENTO_URL}/turmas")
        p_resp = requests.get(f"{GERENCIAMENTO_URL}/professores")
        turmas = t_resp.json()
        profs = p_resp.json()

        if not any(t["id"] == turma_id for t in turmas):
            return jsonify({"error": "Turma inexistente"}), 400
        if not any(p["id"] == professor_id for p in profs):
            return jsonify({"error": "Professor inexistente"}), 400
    except Exception as e:
        return jsonify({"error": "Falha ao comunicar com o serviço de gerenciamento", "details": str(e)}), 500

    atividade = Atividade(
        descricao=data["descricao"],
        peso=data["peso"],
        prazo=data["prazo"],
        turma_id=turma_id,
        professor_id=professor_id
    )
    db.session.add(atividade)
    db.session.commit()
    return jsonify({"message": "Atividade criada", "id": atividade.id}), 201

def update_atividade(id):
    data = request.json
    atividade = Atividade.query.get_or_404(id)
    atividade.descricao = data.get("descricao", atividade.descricao)
    atividade.peso = data.get("peso", atividade.peso)
    atividade.prazo = data.get("prazo", atividade.prazo)
    db.session.commit()
    return jsonify({"message": "Atividade atualizada"})

def delete_atividade(id):
    atividade = Atividade.query.get_or_404(id)
    db.session.delete(atividade)
    db.session.commit()
    return jsonify({"message": "Atividade removida"})

# ------------------------------
# CRUD Notas
# ------------------------------
def get_notas():
    notas = Nota.query.all()
    return jsonify([
        {"id": n.id, "valor": n.valor, "aluno_id": n.aluno_id, "atividade_id": n.atividade_id}
        for n in notas
    ])

def create_nota():
    data = request.json
    nota = Nota(valor=data["valor"], aluno_id=data["aluno_id"], atividade_id=data["atividade_id"])
    db.session.add(nota)
    db.session.commit()
    return jsonify({"message": "Nota registrada", "id": nota.id}), 201

def update_nota(id):
    data = request.json
    nota = Nota.query.get_or_404(id)
    nota.valor = data.get("valor", nota.valor)
    db.session.commit()
    return jsonify({"message": "Nota atualizada"})

def delete_nota(id):
    nota = Nota.query.get_or_404(id)
    db.session.delete(nota)
    db.session.commit()
    return jsonify({"message": "Nota removida"})