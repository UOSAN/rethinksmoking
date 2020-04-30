from unittest import mock
from http import HTTPStatus


class TestPostWorkerRoute:
    def test_bad_request(self, app):
        # Verify that 400 Bad Request is returned on a bad request
        with app.app_context():
            client = app.test_client()
            response = client.post('/worker', data='some garbage test data', content_type='application/text')
            assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_incomplete_object(self, app):
        bad_worker = {'bad_field': 'val'}
        # Currently 200 OK is returned when an incomplete object is received
        with mock.patch('rethinksmoking.orm.mturk_worker.MturkWorker.add') as mock_add:
            with app.app_context():
                client = app.test_client()
                response = client.post('/worker', json=bad_worker, content_type='application/json')
                assert response.status_code == HTTPStatus.OK

    def test_success(self, app):
        actual_worker = {'age': 10, 'gender': 'Female', 'race': 'Hispanic and/or Latinx', 'ethnicity': 'Unknown',
                         'english_primary_language': True, 'education_level': 'No schooling completed',
                         'income': '25000', 'household_size': 9, 'ftnd_1': 1, 'ftnd_2': 1, 'ftnd_3': 1, 'ftnd_4': 1,
                         'ftnd_5': 1, 'ftnd_6': 1, 'messages': []}

        # Verify 200 OK is returned when a complete object is received
        with mock.patch('rethinksmoking.orm.mturk_worker.MturkWorker.add') as mock_add:
            with app.app_context():
                client = app.test_client()
                response = client.post('/worker', json=actual_worker, content_type='application/json')
                assert response.status_code == HTTPStatus.OK
