from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialize DB
    db.init_app(app)

    # Import and register routes
    from app.routes.main import main_routes
    app.register_blueprint(main_routes)

    return app
