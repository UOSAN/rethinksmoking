import os.path
from flask import Flask

from .orm.database import db
from .route import bp


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        try:
            db_connection = os.environ['DB_CONNECTION']
            db_host = os.environ['DB_HOST']
            db_database = os.environ['DB_DATABASE']
            db_user = os.environ['DB_USERNAME']
            db_password = os.environ['DB_PASSWORD']
            db_uri = f'{db_connection}://{db_user}:{db_password}@{db_host}/{db_database}'
        except KeyError as e:
            print(e)
            db_uri = 'sqlite:///:memory:'

        if os.environ.get('MYSQL_SSL') is not None:
            ca_path = os.path.join(app.instance_path, 'BaltimoreCyberTrustRoot.crt.pem')
            db_uri = f'{db_uri}?ssl_ca={ca_path}'

        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(bp)

    db.init_app(app)
    with app.app_context():
        db.create_all()
        return app


flask_app = create_app()
