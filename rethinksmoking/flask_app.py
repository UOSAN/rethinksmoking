from flask import Flask

from .orm.database import db
from .rethinkconfig import RethinkConfig
from .worker import bp


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        config = RethinkConfig(path=app.instance_path)
        app.config.from_mapping(RETHINKCONFIG=config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(bp)

    db.init_app(app)
    return app


flask_app = create_app()
