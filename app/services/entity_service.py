import requests
from flask import current_app, g, jsonify

def create_entity_for_customer(customer_id, payload):
    url = f"{current_app.config['API_HOST']}/v1/customers/{customer_id}/entities?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.post(url, json=payload, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to create entity", "details": str(e)}), 500


def upload_entity_document(customer_id, entity_id, file):
    url = f"{current_app.config['API_HOST']}/v1/customers/{customer_id}/entities/{entity_id}/documents?apikey={current_app.config['API_KEY']}"
    files = {'document': (file.filename, file.stream, file.mimetype)}
    headers = {'Authorization': g.auth_headers['Authorization']}

    try:
        response = requests.post(url, files=files, headers=headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Document upload failed", "details": str(e)}), 500


def get_entity_documents(customer_id, entity_id):
    url = f"{current_app.config['API_HOST']}/v1/customers/{customer_id}/entities/{entity_id}/documents?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.get(url, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch documents", "details": str(e)}), 500


def delete_entity_document(customer_id, entity_id, doc_id):
    url = f"{current_app.config['API_HOST']}/v1/customers/{customer_id}/entities/{entity_id}/documents/{doc_id}?apikey={current_app.config['API_KEY']}"
    try:
        response = requests.delete(url, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify({"message": "Document deleted"}), 200
    except requests.RequestException as e:
        return jsonify({"error": "Failed to delete document", "details": str(e)}), 500