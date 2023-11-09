from flask import Flask
from .main import main_bp

def create_app():
    app = Flask(__name__)

    # Blueprint 등록
    app.register_blueprint(main_bp, url_prefix='/main')

    return app