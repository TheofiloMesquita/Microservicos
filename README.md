# Sistema de Microsserviços Flask — Gestão Escolar

Este projeto implementa um ecossistema de **3 microsserviços independentes**:
1. **Gerenciamento:** CRUD de Professores, Turmas e Alunos.
2. **Reservas:** CRUD de Reservas de Salas, vinculado às Turmas.
3. **Atividades:** CRUD de Atividades e Notas, vinculadas a Turmas e Professores.

## 🧱 Arquitetura
- Cada serviço segue o padrão **MVC (Model-View-Controller)**.
- Cada um possui **banco SQLite próprio**.
- Comunicação entre serviços via **HTTP** (biblioteca `requests`).
- Documentação interativa via **Swagger** (`/apidocs`).

## 🐳 Execução com Docker
```bash
docker-compose up --build