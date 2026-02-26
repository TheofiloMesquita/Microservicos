# 🏗 Sistema de Microsserviços Flask — Gestão Escolar

Este projeto implementa uma arquitetura baseada em microsserviços, composta por três serviços independentes que juntos formam um sistema completo de gestão escolar.

Cada serviço possui seu próprio banco de dados, lógica de negócio isolada e comunicação via HTTP.

---

## 📦 Microsserviços

### 1️⃣ Gerenciamento
Responsável pelo CRUD de:
- Professores
- Turmas
- Alunos

### 2️⃣ Reservas
Responsável pelo CRUD de:
- Reservas de salas
- Vinculação com Turmas via comunicação HTTP

### 3️⃣ Atividades
Responsável pelo CRUD de:
- Atividades
- Notas
- Associação com Professores e Turmas

---

## 🧠 Arquitetura

- Padrão MVC (Model-View-Controller)
- Banco de dados independente por serviço (SQLite)
- Comunicação entre serviços via HTTP (biblioteca `requests`)
- Documentação interativa via Swagger em `/apidocs`
- Orquestração com Docker Compose

---

## 🐳 Execução com Docker

### Subir ambiente:

```bash
docker-compose up --build
```

### 1. **Pré-requisitos**
Certifique-se de ter o **Docker** e o **Docker Compose** instalados.  
Você pode baixar o Docker [aqui](https://www.docker.com/products/docker-desktop).

---

### 2. **Subindo o ambiente**

Após clonar o repositório, entre na pasta principal do projeto e execute:

```bash
docker-compose up --build
```

---

### 3. **Acessando Serviços**

Após a inicialização, os microsserviços estarão disponíveis nos seguintes endereços:

Serviço	URL	Swagger

```bash
Gerenciamento	http://localhost:5000
	http://localhost:5000/apidocs
```

```bash
Reservas	http://localhost:5001
	http://localhost:5001/apidocs
```

```bash
Atividades	http://localhost:5002
	http://localhost:5002/apidocs
```

---

### 4. **Testando Integração**

Cada microsserviço é independente, mas se comunicam entre si via HTTP.

Exemplo de fluxo integrado:

Gerenciamento cadastra Professores, Alunos e Turmas.

Reservas utiliza o ID da Turma fornecido pelo serviço de Gerenciamento para criar uma reserva de sala.

Atividades utiliza o ID do Professor e o ID da Turma para vincular atividades e notas.

---

### 5. **Parando Serviços**

Para encerrar a execução e remover os containers:

```bash
docker-compose down
```

Esse comando irá parar todos os microsserviços e limpar os containers criados.

---

🧠 Arquitetura e Design

MVC: separação clara entre Modelos, Controladores e Rotas.

Banco de dados independente: cada microsserviço usa seu próprio arquivo SQLite.

Comunicação HTTP: integração entre microsserviços feita via requests.

Swagger: documentação automática acessível em /apidocs para cada serviço.

---

🧩 Instruções Rápidas
Ação	Comando
Subir o ambiente	docker-compose up --build
Parar e limpar containers	docker-compose down

```bash
Acessar Swagger Gerenciamento	http://localhost:5000/apidocs
```

```bash
Acessar Swagger Reservas	http://localhost:5001/apidocs
```

```bash
Acessar Swagger Atividades	http://localhost:5002/apidocs
```

---

📋 Conclusão

Este sistema demonstra uma arquitetura de microsserviços Flask aplicada à Gestão Escolar, com três serviços independentes que se comunicam entre si:

Gerenciamento: base de dados de Professores, Alunos e Turmas.

Reservas: controle de uso das salas.

Atividades: registro de atividades e notas.

A arquitetura modular garante baixo acoplamento, fácil manutenção e escalabilidade, permitindo que cada serviço evolua de forma independente.
