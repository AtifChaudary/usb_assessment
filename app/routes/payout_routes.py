from flask import Blueprint, request, jsonify
from app.services.payout_service import create_payout_transaction

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
