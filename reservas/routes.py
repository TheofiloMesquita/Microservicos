from flask import Blueprint
import controllers as ctrl

routes = Blueprint('routes', __name__)

@routes.route('/reservas', methods=['GET'])
def get_reservas():
    """
    ---
    tags:
      - Reservas
    summary: Lista todas as reservas
    responses:
      200:
        description: Lista de reservas retornada com sucesso
    """
    return ctrl.get_reservas()

@routes.route('/reservas', methods=['POST'])
def create_reserva():
    """
    ---
    tags:
      - Reservas
    summary: Cria uma nova reserva de sala
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            num_sala:
              type: string
            data:
              type: string
            turma_id:
              type: integer
    responses:
      201:
        description: Reserva criada com sucesso
    """
    return ctrl.create_reserva()