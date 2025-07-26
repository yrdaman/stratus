from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Load configuration
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
        DATABASE='path_to_your_database'
    )

    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app