from http import HTTPStatus
from unittest import mock


class TestGetRatingRoute:
    def test_success_rating(self, app):
        with mock.patch('sqlalchemy.orm.query.Query.all', return_value=[]) as mock_all:
            with app.app_context():
                client = app.test_client()
                response = client.get('/rating')
                assert response.status_code == HTTPStatus.OK
                assert mock_all.called
