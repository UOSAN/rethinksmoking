import os.path
import pytest
import tempfile

from rethinksmoking.flask_app import create_app
from rethinksmoking.orm.database import db as _db

TEST_DATABASE = 'rethinksmoking_test.db'
TEST_DATABASE_PATH = os.path.join(tempfile.gettempdir(), TEST_DATABASE)
TEST_DATABASE_URI = 'sqlite:///' + TEST_DATABASE_PATH


@pytest.fixture(scope='session')
def app():
    """Session-wide test `Flask` application"""
    app = create_app(test_config={
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI
    })

    yield app


@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    if os.path.exists(TEST_DATABASE_PATH):
        os.unlink(TEST_DATABASE_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TEST_DATABASE_PATH)

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture()
def client(app):
    """Test `Flask` client"""
    return app.test_client()
