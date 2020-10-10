from typing import TypeVar

from flask import Flask

from .routes import api
from .types import ServerConfig


def init_app(config: TypeVar(ServerConfig)):
    app = Flask(__name__)
    app.config.from_object(config)

    api.init_app(app)

    return app
