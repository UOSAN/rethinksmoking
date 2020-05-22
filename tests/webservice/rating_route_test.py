from http import HTTPStatus
from unittest import mock

from rethinksmoking.orm.message import Message
from rethinksmoking.orm.enums import Condition


class TestGetRatingRoute:
    def test_success_rating(self, app):
        with mock.patch('sqlalchemy.orm.query.Query.all', return_value=[]) as mock_all, \
                app.app_context():
            client = app.test_client()
            response = client.get('/rating')
            assert response.status_code == HTTPStatus.OK
            assert mock_all.called


class TestPostRatingRoute:
    def test_bad_request(self, app):
        # Verify that 400 Bad Request is returned on a bad request
        with app.app_context():
            client = app.test_client()
            response = client.post('/rating', data='some garbage test data', content_type='application/text')
            assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_incomplete_object(self, app):
        bad_object = {'bad_field': 'val'}
        # Return 400 Bad Request when an incomplete object is sent
        with mock.patch('rethinksmoking.orm.rating.Rating.add'), \
                app.app_context():
            client = app.test_client()
            response = client.post('/rating', json=bad_object, content_type='application/json')
            assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_success(self, app):
        actual_rating = {'helpfulness': 10, 'relatability': 0, 'familiarity': 3, 'message_id': 4}

        # Verify 200 OK is returned when a complete object is received
        message = Message(id=5, message_content='', condition=Condition.DownRegulation)
        with mock.patch('sqlalchemy.orm.query.Query.get', return_value=message) as mock_get, \
                mock.patch('sqlalchemy.orm.collections.InstrumentedList.append') as mock_append, \
                mock.patch('rethinksmoking.orm.rating.Rating.add') as mock_add, \
                app.app_context():
            client = app.test_client()
            response = client.post('/rating', json=actual_rating, content_type='application/json')
            assert response.status_code == HTTPStatus.OK
            assert mock_get.called
            assert mock_append.called
            assert mock_add.called
