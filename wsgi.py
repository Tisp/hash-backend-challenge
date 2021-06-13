import os

from src.infra.http.app import create_app

app = create_app(os.environ["FLASK_CONFIG"])
