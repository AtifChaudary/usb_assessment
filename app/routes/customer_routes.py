from flask import Blueprint, request, jsonify
from app.serializers.payload_schemas import CustomerSchema
from app.services.customer_service import (
    create_customer_in_buckzy,
    update_customer_in_buckzy,
    get_customer_by_id,
    list_all_customers,
    list_active_customers
)

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
          $ref: '#/definitions/Customer'
    responses:
      200:
        description: Customer created successfully
      400:
        description: Invalid input
    """
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    return create_customer_in_buckzy(data)


@customer_bp.route('/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """
    Update Customer
    ---
    tags:
      - Customers
    parameters:
      - name: customer_id
        in: path
        type: string
        required: true
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/Customer'
    responses:
      200:
        description: Customer updated successfully
    """
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    return update_customer_in_buckzy(customer_id, data)


@customer_bp.route('/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    """
    Get Customer by ID
    ---
    tags:
      - Customers
    parameters:
      - name: customer_id
        in: path
        type: string
        required: true
    responses:
      200:
        description: Customer details
    """
    return get_customer_by_id(customer_id)


@customer_bp.route('/', methods=['GET'])
def get_all_customers():
    """
    List All Customers
    ---
    tags:
      - Customers
    responses:
      200:
        description: List of customers
    """
    return list_all_customers()


@customer_bp.route('/active', methods=['GET'])
def get_active_customers():
    """
    List Active Customers
    ---
    tags:
      - Customers
    responses:
      200:
        description: List of active customers
    """
    return list_active_customers()
