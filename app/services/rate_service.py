import requests
from flask import current_app, g, jsonify

def fetch_spot_rate(from_currency, to_currency):
    url = f"{current_app.config['API_HOST']}/v1/rates/spot?fromCurrency={from_currency}&toCurrency={to_currency}&apikey={current_app.config['API_KEY']}"
    try:
        response = requests.get(url, headers=g.auth_headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch spot rate", "details": str(e)}), 500
