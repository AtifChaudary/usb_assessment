from flask import Blueprint, request, jsonify
from app.services.rate_service import fetch_spot_rate

rate_bp = Blueprint('rates', __name__)

@rate_bp.route('/', methods=['GET'])
def get_spot_rate():
    """
    Get SPOT Rate
    ---
    tags:
      - Spot Rates
    parameters:
      - name: fromCurrency
        in: query
        type: string
        required: true
        description: Currency to convert from (e.g., USD)
      - name: toCurrency
        in: query
        type: string
        required: true
        description: Currency to convert to (e.g., INR)
    responses:
      200:
        description: Spot rate fetched successfully
        examples:
          application/json: {"rate": 82.45}
      400:
        description: Missing required parameters
      403:
        description: Authorization failed
    """
    from_currency = request.args.get('fromCurrency')
    to_currency = request.args.get('toCurrency')

    if not from_currency or not to_currency:
        return jsonify({"error": "Missing fromCurrency or toCurrency"}), 400

    return fetch_spot_rate(from_currency, to_currency)
