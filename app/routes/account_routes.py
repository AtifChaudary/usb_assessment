from flask import Blueprint
from app.services.account_service import get_account_by_client_id

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