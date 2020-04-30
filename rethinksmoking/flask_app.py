import os.path
from flask import Flask

from .orm.database import db
from .worker import bp


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        try:
            app.config.from_pyfile('config.py')
            path = os.path.join(app.instance_path, app.config['SQLALCHEMY_DATABASE_NAME'])
        except IOError as e:
            print(e)
            path = ':memory:'
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path}'
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(bp)

    db.init_app(app)
    return app


flask_app = create_app()
