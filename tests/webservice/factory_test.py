from rethinksmoking.flask_app import create_app


def test_create_app():
    test_config = {'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'}

    app = create_app(test_config)
    assert app.testing
    assert len(app.blueprints) == 1
    assert app.config['SQLALCHEMY_DATABASE_URI'] == test_config['SQLALCHEMY_DATABASE_URI']
