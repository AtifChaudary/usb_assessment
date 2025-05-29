import requests
from flask import current_app, g, jsonify, request
from datetime import datetime, timedelta

_token = None
_token_expiry = None

def init_auth(app):
    @app.before_request
    def fetch_token():
        global _token, _token_expiry
        print(f"Incoming {request.method} {request.path}")  # debug route info
        try:
            if not _token or datetime.utcnow() >= _token_expiry:
                auth_url = f"{current_app.config['AUTH_HOST']}/token?apikey={current_app.config['API_KEY']}"
                payload = {
                    'grant_type': 'password',
                    'client_id': current_app.config['CLIENT_ID'],
                    'client_secret': current_app.config['CLIENT_SECRET'],
                    'username': current_app.config['USERNAME'],
                    'password': current_app.config['PASSWORD']
                }
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}

                response = requests.post(auth_url, data=payload, headers=headers, timeout=current_app.config.get('TIMEOUT', 30))
                response.raise_for_status()
                token_data = response.json()

                _token = token_data['access_token']
                _token_expiry = datetime.utcnow() + timedelta(seconds=token_data['expires_in'])

            # token is set
            g.token = _token
            g.auth_headers = {
                'Authorization': f'Bearer {_token}',
                'Content-Type': 'application/json'
            }

        except Exception as e:
            return jsonify({
                "error": "Authorization failed",
                "details": str(e)
            }), 403
