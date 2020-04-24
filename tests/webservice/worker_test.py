from unittest import mock
from http import HTTPStatus


def test_add_worker_and_messages_bad_request(app):
    # Verify that 400 Bad Request is returned on a bad request
    with app.app_context():
        client = app.test_client()
        response = client.post('/worker/message', data='some garbage test data', content_type='application/text')
        assert response.status_code == HTTPStatus.BAD_REQUEST


def test_add_worker_and_messages_incomplete_object(app):
    # Currently 200 OK is returned when an incomplete object is sent
    with mock.patch('rethinksmoking.orm.mturk_worker.MturkWorker.add') as mock_add:
        with app.app_context():
            client = app.test_client()
            response = client.post('/worker/message', json={'bad_field': 'bad_value'}, content_type='application/json')
            assert response.status_code == HTTPStatus.OK
