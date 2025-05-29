from flask import Blueprint
from app.services.account_service import (
    get_account_by_client_id,
    get_account_balance,
    create_buckzy_account
)
account_bp = Blueprint('accounts', __name__)

@account_bp.route('/<client_id>', methods=['GET'])
def get_account_details(client_id):
    """
    Get Buckzy Account Information
    ---
    tags:
      - Accounts
    parameters:
      - name: client_id
        in: path
        type: string
        required: true
    responses:
      200:
        description: Account information retrieved
      403:
        description: Authorization failed
    """
    return get_account_by_client_id(client_id)


@account_bp.route('/', methods=['POST'])
def create_account():
    """
    Create Buckzy Account
    ---
    tags:
      - Accounts
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - clientId
            - currency
          properties:
            clientId:
              type: string
            currency:
              type: string
    responses:
      200:
        description: Account created successfully
      403:
        description: Authorization failed
    """
    data = request.get_json()
    if not data.get("clientId") or not data.get("currency"):
        return jsonify({"error": "Missing clientId or currency"}), 400
    return create_buckzy_account(data)


@account_bp.route('/<client_id>/balance', methods=['GET'])
def get_balance(client_id):
    """
    Get Account Balance
    ---
    tags:
      - Accounts
    parameters:
      - name: client_id
        in: path
        required: true
        type: string
    responses:
      200:
        description: Balance information retrieved
      403:
        description: Authorization failed
    """
    return get_account_balance(client_id)
