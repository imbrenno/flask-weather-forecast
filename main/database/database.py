from flask import g
from pymongo import MongoClient
from main.utils.settings import Settings
from main.utils.enums.dot_env import DotEnvEnum


def get_db():
    if "db" not in g:
        client = MongoClient(Settings.get(DotEnvEnum.MONGO_URI.value))
        g.db = client["flask-basic"]

    return g.db
