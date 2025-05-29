from flask import Blueprint, request, jsonify
from app.serializers.payload_schemas import EntitySchema
from app.services.entity_service import (
    create_entity_for_customer,
    upload_entity_document,
    get_entity_documents,
    delete_entity_document
)

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


@entity_bp.route('/<customer_id>/entities/<entity_id>/documents', methods=['POST'])
def upload_entity_doc_route(customer_id, entity_id):
    """
    Upload Entity Document
    ---
    tags:
      - Entity Documents
    consumes:
      - multipart/form-data
    parameters:
      - name: customer_id
        in: path
        required: true
        type: string
      - name: entity_id
        in: path
        required: true
        type: string
      - name: document
        in: formData
        required: true
        type: file
        description: The document file to upload
    responses:
      200:
        description: Document uploaded successfully
      400:
        description: Missing file in request
      403:
        description: Authorization failed
    """
    file = request.files.get('document')
    if not file:
        return jsonify({"error": "Missing document file"}), 400
    return upload_entity_document(customer_id, entity_id, file)


@entity_bp.route('/<customer_id>/entities/<entity_id>/documents', methods=['GET'])
def get_entity_docs_route(customer_id, entity_id):
    """
    Get Entity Documents
    ---
    tags:
      - Entity Documents
    parameters:
      - name: customer_id
        in: path
        required: true
        type: string
      - name: entity_id
        in: path
        required: true
        type: string
    responses:
      200:
        description: List of uploaded documents
      403:
        description: Authorization failed
    """
    return get_entity_documents(customer_id, entity_id)


@entity_bp.route('/<customer_id>/entities/<entity_id>/documents/<doc_id>', methods=['DELETE'])
def delete_entity_doc_route(customer_id, entity_id, doc_id):
    """
    Delete Entity Document
    ---
    tags:
      - Entity Documents
    parameters:
      - name: customer_id
        in: path
        required: true
        type: string
      - name: entity_id
        in: path
        required: true
        type: string
      - name: doc_id
        in: path
        required: true
        type: string
    responses:
      200:
        description: Document deleted successfully
      403:
        description: Authorization failed
    """
    return delete_entity_document(customer_id, entity_id, doc_id)
