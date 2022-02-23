import logging
import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

logging.basicConfig()
logger = logging.getLogger("sqlalchemy.engine")
logger.setLevel(logging.DEBUG)


def create_app():
    app = Flask(__name__)
    app_settings = os.environ.get("APP_SETTINGS", "project.config.DevelopmentConfig")
    app.config.from_object(app_settings)

    db.init_app(app)
    migrate.init_app(app, db)

    from project.api import api

    api.init_app(app)

    @app.shell_context_processor
    def ctx():  # pragma: no cover
        return {"app": app, "db": db}

    return app
