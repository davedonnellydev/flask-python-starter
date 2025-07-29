from flask import Flask
from app.proxy import proxy_bp  # import your blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(proxy_bp)
    return app
