from flask import Flask
from main.utils.log import setup_logger
from main.utils.settings import Settings
from main.utils.enums.dot_env import DotEnvEnum
from main.controllers import blueprints_ctrl
from pymongo import MongoClient


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path="/static",
        static_folder="static",
        instance_relative_config=True,
    )
    log = setup_logger()

    app.config["MONGO_URI"] = Settings.get(DotEnvEnum.MONGO_URI.value)
    log.info(f"Mongo URI: {app.config['MONGO_URI']}")

    client = MongoClient(Settings.get(DotEnvEnum.MONGO_URI.value))
    db = client["flask-basic"]
    log.info(f"Setting, 'client' {client} ")

    # create collections
    models = [
        "direct_geocoding",
        "weather_forecast",
    ]
    for collection_name in models:
        log.info(f"collection_name: {collection_name}")
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            log.info(f"Created collection: {collection_name}")
        else:
            log.info(f"Collection already exists: {collection_name}")

    if test_config:
        app.config.update(test_config)

    for bp in blueprints_ctrl:
        app.register_blueprint(bp)

    return app
