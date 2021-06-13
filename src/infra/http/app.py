from flask import Flask
from src.infra.http.controllers import checkout


def create_app(config_name):

    app = Flask(__name__)

    config_module = f"src.infra.http.config.{config_name.capitalize()}Config"
    app.config.from_object(config_module)
    app.register_blueprint(checkout.blueprint)

    return app
