from flask import Blueprint, request, jsonify
from app.services.payout_service import create_payout_transaction, get_payout_transaction_status

payout_bp = Blueprint('payouts', __name__)

@payout_bp.route('/', methods=['POST'])
def create_payout():
    """
    Create a Payout Transaction
    ---
    tags:
      - Payouts
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Payout
          required:
            - amount
            - currency
            - recipient
          properties:
            amount:
              type: number
            currency:
              type: string
            recipient:
              type: string
    responses:
      200:
        description: Payout created successfully
      400:
        description: Invalid input
      403:
        description: Authorization failed
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    return create_payout_transaction(data)


@payout_bp.route('/status/<txn_id>', methods=['GET'])
def get_payout_status(txn_id):
    """
    Get Payout Transaction Status
    ---
    tags:
      - Payouts
    parameters:
      - name: txn_id
        in: path
        required: true
        type: string
        description: Transaction ID of the payout
    responses:
      200:
        description: Payout status retrieved successfully
      403:
        description: Authorization failed
    """
    return get_payout_transaction_status(txn_id)