import pytest

from rethinksmoking.flask_app import create_app
from rethinksmoking.rethinkconfig import RethinkConfig


@pytest.fixture
def app():
    config = RethinkConfig(path=None)

    app = create_app(test_config={
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'test_uri',
        'RETHINKCONFIG': config
    })

    yield app
