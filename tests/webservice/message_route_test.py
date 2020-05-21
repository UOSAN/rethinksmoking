from http import HTTPStatus
from unittest import mock


class TestGetMessageRoute:
    def test_success_message(self, app):
        with mock.patch('sqlalchemy.orm.query.Query.all', return_value=[]) as mock_all, \
                app.app_context():
            client = app.test_client()
            response = client.get('/message')
            assert response.status_code == HTTPStatus.OK
            assert mock_all.called
