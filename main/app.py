from flask import Flask
from main.utils.settings import Settings
from main.utils.enums.dot_env import DotEnvEnum
from main.controllers import blueprints_ctrl


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path="/static",
        static_folder="static",
        instance_relative_config=True,
    )

    app.config["MONGO_URI"] = Settings.get(DotEnvEnum.MONGO_URI.value)
    print(f"Mongo URI: {app.config['MONGO_URI']}")

    if test_config:
        app.config.update(test_config)

    for bp in blueprints_ctrl:
        app.register_blueprint(bp)

    return app
