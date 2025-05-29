import requests
from flask import current_app, g, jsonify

def create_payout_transaction(payload):
    url = f"{current_app.config['API_HOST']}/v1/transactions/payout?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.post(url, json=payload, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to initiate payout transaction", "details": str(e)}), 500

def get_payout_transaction_status(txn_id):
    url = f"{current_app.config['API_HOST']}/v1/transactions/payout/status/{txn_id}?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.get(url, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch payout status", "details": str(e)}), 500
