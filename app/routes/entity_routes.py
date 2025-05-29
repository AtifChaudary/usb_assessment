from flask import Blueprint, request, jsonify
from app.serializers.payload_schemas import EntitySchema
from app.services.entity_service import create_entity_for_customer

entity_bp = Blueprint('entities', __name__)
schema = EntitySchema()

@entity_bp.route('/<customer_id>', methods=['POST'])
def create_entity(customer_id):
    """
    Create Entity Document for a Customer
    ---
    tags:
      - Entities
    parameters:
      - name: customer_id
        in: path
        type: string
        required: true
      - name: body
        in: body
        required: true
        schema:
          id: Entity
          required:
            - documentType
            - documentUrl
          properties:
            documentType:
              type: string
            documentUrl:
              type: string
    responses:
      200:
        description: Entity document created
      403:
        description: Authorization failed
    """
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    return create_entity_for_customer(customer_id, data)
