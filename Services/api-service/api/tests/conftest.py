import pytest
from api import create_app

#
#   Pedro Díaz | 23-05-2023
#   conftest.py definido para la realización de pruebas unitarias. 
#   

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
    