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