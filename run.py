from flask import Flask
from app.routes.customer_routes import customer_bp
from app.routes.entity_routes import entity_bp
from app.routes.rate_routes import rate_bp
from app.routes.account_routes import account_bp
from app.routes.payout_routes import payout_bp
from app.utils.auth import init_auth
from app.utils.error_handlers import register_error_handlers
from flasgger import Swagger


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Initialize Auth
    init_auth(app)

    # Enable Swagger
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": '/api/v1',
                "route": '/api/v1',
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/"
    }

    Swagger(app, config=swagger_config)

    # Register blueprints
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(entity_bp, url_prefix='/entities')
    app.register_blueprint(rate_bp, url_prefix='/spot-rates')
    app.register_blueprint(account_bp, url_prefix='/accounts')
    app.register_blueprint(payout_bp, url_prefix='/payouts')

    # Register error handlers
    register_error_handlers(app)

    return app


if __name__ == '__main__':
    application = create_app()
    application.run(debug=True)
