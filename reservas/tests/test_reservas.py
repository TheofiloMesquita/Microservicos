import pytest
from app import app, db
from models import Reserva

@pytest.fixture
def client(monkeypatch):
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def mock_get_turmas_ok(url):
    class MockResponse:
        def json(self): return [{"id": 1, "nome": "Turma A"}]
    return MockResponse()

def test_criar_reserva(client, monkeypatch):
    monkeypatch.setattr("controllers.requests.get", mock_get_turmas_ok)
    resp = client.post('/reservas', json={"num_sala": "101", "data": "2025-10-31", "turma_id": 1})
    assert resp.status_code == 201
    assert b"Reserva criada" in resp.data