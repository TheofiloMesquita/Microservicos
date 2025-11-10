from flask import Blueprint
import controllers as ctrl

routes = Blueprint('routes', __name__)

# ---------------- PROFESSORES ----------------
@routes.route('/professores', methods=['GET'])
def get_professores():
    """
    ---
    tags:
      - Professores
    summary: Lista todos os professores
    responses:
      200:
        description: Lista de professores retornada com sucesso
    """
    return ctrl.get_professores()

@routes.route('/professores', methods=['POST'])
def create_professor():
    """
    ---
    tags:
      - Professores
    summary: Cria um novo professor
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome:
              type: string
            email:
              type: string
    responses:
      201:
        description: Professor criado com sucesso
    """
    return ctrl.create_professor()

@routes.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    """
    ---
    tags:
      - Professores
    summary: Atualiza um professor existente
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome:
              type: string
            email:
              type: string
    responses:
      200:
        description: Professor atualizado com sucesso
    """
    return ctrl.update_professor(id)

@routes.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    """
    ---
    tags:
      - Professores
    summary: Remove um professor
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Professor removido com sucesso
    """
    return ctrl.delete_professor(id)

# ---------------- TURMAS ----------------
@routes.route('/turmas', methods=['GET'])
def get_turmas():
    """
    ---
    tags:
      - Turmas
    summary: Lista todas as turmas
    responses:
      200:
        description: Lista de turmas retornada com sucesso
    """
    return ctrl.get_turmas()

@routes.route('/turmas', methods=['POST'])
def create_turma():
    """
    ---
    tags:
      - Turmas
    summary: Cria uma nova turma
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome:
              type: string
            professor_id:
              type: integer
    responses:
      201:
        description: Turma criada com sucesso
    """
    return ctrl.create_turma()

@routes.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    """
    ---
    tags:
      - Turmas
    summary: Atualiza uma turma existente
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome:
              type: string
            professor_id:
              type: integer
    responses:
      200:
        description: Turma atualizada com sucesso
    """
    return ctrl.update_turma(id)

@routes.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    """
    ---
    tags:
      - Turmas
    summary: Remove uma turma
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Turma removida com sucesso
    """
    return ctrl.delete_turma(id)

# ---------------- ALUNOS ----------------
@routes.route('/alunos', methods=['GET'])
def get_alunos():
    """
    ---
    tags:
      - Alunos
    summary: Lista todos os alunos
    responses:
      200:
        description: Lista de alunos retornada com sucesso
    """
    return ctrl.get_alunos()

@routes.route('/alunos', methods=['POST'])
def create_aluno():
    """
    ---
    tags:
      - Alunos
    summary: Cria um novo aluno
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome:
              type: string
            email:
              type: string
            turma_id:
              type: integer
    responses:
      201:
        description: Aluno criado com sucesso
    """
    return ctrl.create_aluno()

@routes.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    """
    ---
    tags:
      - Alunos
    summary: Atualiza um aluno existente
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            nome:
              type: string
            email:
              type: string
            turma_id:
              type: integer
    responses:
      200:
        description: Aluno atualizado com sucesso
    """
    return ctrl.update_aluno(id)

@routes.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    """
    ---
    tags:
      - Alunos
    summary: Remove um aluno
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Aluno removido com sucesso
    """
    return ctrl.delete_aluno(id)