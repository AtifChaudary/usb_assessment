import requests
from flask import current_app, g, jsonify

def create_customer_in_buckzy(payload):
    url = f"{current_app.config['API_HOST']}/v1/customers?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.post(url, json=payload, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to create customer", "details": str(e)}), 500
