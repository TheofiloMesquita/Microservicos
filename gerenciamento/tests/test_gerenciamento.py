import pytest
from app import app, db
from models import Professor, Turma, Aluno

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_criar_professor(client):
    resp = client.post('/professores', json={"nome": "Maria", "email": "maria@escola.com"})
    assert resp.status_code == 201
    assert b"Professor criado" in resp.data

def test_criar_turma(client):
    p = Professor(nome="Carlos", email="carlos@escola.com")
    db.session.add(p)
    db.session.commit()
    resp = client.post('/turmas', json={"nome": "Turma A", "professor_id": p.id})
    assert resp.status_code == 201

def test_criar_aluno(client):
    p = Professor(nome="Ana", email="ana@escola.com")
    db.session.add(p)
    db.session.commit()
    t = Turma(nome="Turma B", professor_id=p.id)
    db.session.add(t)
    db.session.commit()
    resp = client.post('/alunos', json={"nome": "João", "email": "joao@escola.com", "turma_id": t.id})
    assert resp.status_code == 201