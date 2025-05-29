import requests
from flask import current_app, g, jsonify

def get_account_by_client_id(client_id):
    url = f"{current_app.config['API_HOST']}/v1/accounts/{client_id}?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.get(url, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to retrieve account details", "details": str(e)}), 500

def create_buckzy_account(payload):
    url = f"{current_app.config['API_HOST']}/v1/accounts?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.post(url, json=payload, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to create account", "details": str(e)}), 500


def get_account_balance(client_id):
    url = f"{current_app.config['API_HOST']}/v1/accounts/{client_id}/balance?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.get(url, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to retrieve balance", "details": str(e)}), 500
