from flask import Blueprint
import controllers as ctrl

routes = Blueprint('routes', __name__)

# ---------------- ATIVIDADES ----------------
@routes.route('/atividades', methods=['GET'])
def get_atividades():
    """
    ---
    tags:
      - Atividades
    summary: Lista todas as atividades
    responses:
      200:
        description: Lista de atividades retornada com sucesso
    """
    return ctrl.get_atividades()

@routes.route('/atividades', methods=['POST'])
def create_atividade():
    """
    ---
    tags:
      - Atividades
    summary: Cria uma nova atividade
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            descricao:
              type: string
            peso:
              type: number
            prazo:
              type: string
            turma_id:
              type: integer
            professor_id:
              type: integer
    responses:
      201:
        description: Atividade criada com sucesso
    """
    return ctrl.create_atividade()

# ---------------- NOTAS ----------------
@routes.route('/notas', methods=['GET'])
def get_notas():
    """
    ---
    tags:
      - Notas
    summary: Lista todas as notas
    responses:
      200:
        description: Lista de notas retornada com sucesso
    """
    return ctrl.get_notas()

@routes.route('/notas', methods=['POST'])
def create_nota():
    """
    ---
    tags:
      - Notas
    summary: Registra uma nova nota de aluno
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            valor:
              type: number
            aluno_id:
              type: integer
            atividade_id:
              type: integer
    responses:
      201:
        description: Nota registrada com sucesso
    """
    return ctrl.create_nota()