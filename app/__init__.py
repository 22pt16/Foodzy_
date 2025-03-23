from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Correct DB instance created once here
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Correct DB initialization
    db.init_app(app)

    # Import and register routes correctly
    
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
