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


def update_customer_in_buckzy(customer_id, payload):
    url = f"{current_app.config['API_HOST']}/v1/customers/{customer_id}?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.put(url, json=payload, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to update customer", "details": str(e)}), 500


def get_customer_by_id(customer_id):
    url = f"{current_app.config['API_HOST']}/v1/customers/{customer_id}?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.get(url, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch customer", "details": str(e)}), 500


def list_all_customers():
    url = f"{current_app.config['API_HOST']}/v1/customers?apikey={current_app.config['API_KEY']}&size=999"
    try:
        response = requests.get(url, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to list customers", "details": str(e)}), 500


def list_active_customers():
    url = f"{current_app.config['API_HOST']}/v1/customers?apikey={current_app.config['API_KEY']}&size=999&status=ACTIVE"
    try:
        response = requests.get(url, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to list active customers", "details": str(e)}), 500
