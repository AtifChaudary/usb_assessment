from flask import Blueprint, request, jsonify
from app.serializers.payload_schemas import CustomerSchema
from app.services.customer_service import create_customer_in_buckzy

customer_bp = Blueprint('customers', __name__)
schema = CustomerSchema()

@customer_bp.route('/', methods=['POST'])
def create_customer():
    """
    Create Customer (Individual or Corporate)
    ---
    tags:
      - Customers
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Customer
          required:
            - legalName
            - emailAddress
          properties:
            legalName:
              type: string
            emailAddress:
              type: string
            registrationNumber:
              type: string
            countryOfRegistration:
              type: string
            taxId:
              type: string
    responses:
      200:
        description: Customer created successfully
      400:
        description: Invalid input
      403:
        description: Authorization failed
    """
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    return create_customer_in_buckzy(data)
