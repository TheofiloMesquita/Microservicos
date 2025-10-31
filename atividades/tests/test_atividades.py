import pytest
from app import app, db
from models import Atividade, Nota

@pytest.fixture
def client(monkeypatch):
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def mock_get_professores_ok(url):
    class MockResponse:
        def json(self): return [{"id": 1, "nome": "Carlos"}]
    return MockResponse()

def mock_get_turmas_ok(url):
    class MockResponse:
        def json(self): return [{"id": 2, "nome": "Turma A"}]
    return MockResponse()

def test_criar_atividade(client, monkeypatch):
    monkeypatch.setattr("controllers.requests.get", lambda url: mock_get_turmas_ok(url) if "turmas" in url else mock_get_professores_ok(url))
    resp = client.post('/atividades', json={
        "descricao": "Prova 1",
        "peso": 2,
        "prazo": "2025-11-10",
        "turma_id": 2,
        "professor_id": 1
    })
    assert resp.status_code == 201
    assert b"Atividade criada" in resp.data

def test_criar_nota(client):
    a = Atividade(descricao="Tarefa", peso=1.0, prazo="2025-11-05", turma_id=1, professor_id=1)
    db.session.add(a)
    db.session.commit()
    resp = client.post('/notas', json={"valor": 9.5, "aluno_id": 3, "atividade_id": a.id})
    assert resp.status_code == 201
    assert b"Nota registrada" in resp.data