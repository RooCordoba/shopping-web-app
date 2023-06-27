from main import app
import pytest
from fastapi.testclient import TestClient
from peewee import SqliteDatabase
from src.db import User
import os

MODELS = [User]

test_filepath = 'src/tests/trash_testing_file:foobar_database?mode=memory&cache=shared'
test_database = SqliteDatabase(test_filepath)
User._meta.database = test_database

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(scope='function', autouse=True)
def db_test():
    test_database.connect()
    test_database.create_tables(MODELS)
    yield
    test_database.drop_tables(MODELS)
    test_database.close()

""" @pytest.fixture(scope="session", autouse=True)
def cleanUp(request):
    def remove_file():
        test_database.close()
        if os.path.exists(test_filepath):
            print("lo encontró")
            test_database.close()
            os.remove(test_filepath)
        else:
            print("no lo encontró :(")
    request.addfinalizer(remove_file) """
