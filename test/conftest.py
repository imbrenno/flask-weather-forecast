import pytest
import os
from main.app import create_app

os.environ["PYTHONPATH"] = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)


@pytest.fixture
def app():
    app = create_app(
        {"TESTING": True, "MONGO_URI": "mongodb://mongo:27017/test_db"}
    )
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown_db():
    from pymongo import MongoClient

    client = MongoClient("mongodb://mongo:27017/test_db")
    test_db = client["test_db"]

    # Limpar as coleções antes do teste
    for collection in test_db.list_collection_names():
        test_db.drop_collection(collection)

    yield

    # Limpar as coleções após o teste
    for collection in test_db.list_collection_names():
        test_db.drop_collection(collection)

    # Fechar a conexão do cliente MongoDB
    client.close()
