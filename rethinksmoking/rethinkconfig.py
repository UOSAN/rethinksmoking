import json
import logging
import os


class RethinkConfig:
    """
    Class to read configuration for app from a file
    """

    def __init__(self, path: str = None):
        logging.getLogger().info(f' Configuration path is: {path}')
        self._config_path = path
        self._database_uri = None

    def read_config(self):
        if self._config_path:
            with open(os.path.join(self._config_path, 'config.json')) as f:
                configuration = json.load(f)
                self._database_uri = configuration['SQLALCHEMY_DATABASE_URI']

    def get_database_uri(self):
        if self._database_uri is None:
            self.read_config()
        return self._database_uri
