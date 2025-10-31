from flask import jsonify, request
from models import db, Professor, Turma, Aluno

# CRUD Professor
def get_professores():
    return jsonify([{"id": p.id, "nome": p.nome, "email": p.email} for p in Professor.query.all()])

def create_professor():
    data = request.json
    prof = Professor(nome=data['nome'], email=data['email'])
    db.session.add(prof)
    db.session.commit()
    return jsonify({"message": "Professor criado", "id": prof.id}), 201

def update_professor(id):
    data = request.json
    prof = Professor.query.get_or_404(id)
    prof.nome = data.get('nome', prof.nome)
    prof.email = data.get('email', prof.email)
    db.session.commit()
    return jsonify({"message": "Professor atualizado"})

def delete_professor(id):
    prof = Professor.query.get_or_404(id)
    db.session.delete(prof)
    db.session.commit()
    return jsonify({"message": "Professor removido"})

# CRUD Turma
def get_turmas():
    return jsonify([{"id": t.id, "nome": t.nome, "professor_id": t.professor_id} for t in Turma.query.all()])

def create_turma():
    data = request.json
    turma = Turma(nome=data['nome'], professor_id=data['professor_id'])
    db.session.add(turma)
    db.session.commit()
    return jsonify({"message": "Turma criada", "id": turma.id}), 201

# CRUD Aluno
def get_alunos():
    return jsonify([{"id": a.id, "nome": a.nome, "email": a.email, "turma_id": a.turma_id} for a in Aluno.query.all()])

def create_aluno():
    data = request.json
    aluno = Aluno(nome=data['nome'], email=data['email'], turma_id=data['turma_id'])
    db.session.add(aluno)
    db.session.commit()
    return jsonify({"message": "Aluno criado", "id": aluno.id}), 201