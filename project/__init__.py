import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate db
db = SQLAlchemy()


# app
def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)

    from project.api.ping import ping_blueprint

    app.register_blueprint(ping_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
