import pytest

from rethinksmoking.flask_app import create_app
from rethinksmoking.rethinkconfig import RethinkConfig


@pytest.fixture
def app():
    """Session-wide test `Flask` application"""
    config = RethinkConfig(path=None)

    app = create_app(test_config={
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'test_uri',
        'RETHINKCONFIG': config
    })

    yield app


@pytest.fixture()
def client(app):
    """Test `Flask` client"""
    return app.test_client()
