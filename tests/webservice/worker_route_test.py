from http import HTTPStatus
from unittest import mock


class TestGetWorkerRoute:
    def test_success_worker(self, app):
        with mock.patch('sqlalchemy.orm.query.Query.all', return_value=[]) as mock_all, \
                app.app_context():
            client = app.test_client()
            response = client.get('/worker')
            assert response.status_code == HTTPStatus.OK
            assert mock_all.called


class TestPostWorkerRoute:
    def test_bad_request(self, app):
        # Verify that 400 Bad Request is returned on a bad request
        with app.app_context():
            client = app.test_client()
            response = client.post('/worker', data='some garbage test data', content_type='application/text')
            assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_incomplete_object(self, app):
        bad_worker = {'bad_field': 'val'}
        # Return 400 Bad Request when an incomplete object is sent
        with mock.patch('rethinksmoking.orm.mturk_worker.MturkWorker.add'), \
                app.app_context():
            client = app.test_client()
            response = client.post('/worker', json=bad_worker, content_type='application/json')
            assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_bad_request_enum(self, app):
        # Verify 400 Bad Request is returned when a field expects an enum value integer
        # but gets the enum name string instead.
        actual_worker = {'age': 10, 'gender': 'Female', 'is_hispanic': '1', 'ethnicity': 'Unknown',
                         'is_english_primary_language': 'No', 'education_level': 'HighSchoolNoDiploma',
                         'income': 'Below25', 'household_size': 9, 'ftnd_1': 1, 'ftnd_2': 1, 'ftnd_3': 1, 'ftnd_4': 1,
                         'ftnd_5': 1, 'ftnd_6': 1}

        # Verify 200 OK is returned when a complete object is received
        with mock.patch('rethinksmoking.orm.mturk_worker.MturkWorker.add'), \
                app.app_context():
            client = app.test_client()
            response = client.post('/worker', json=actual_worker, content_type='application/json')
            assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_success(self, app):
        actual_worker = {'age': 10, 'gender': 'Female', 'is_hispanic': '1', 'ethnicity': 'Unknown',
                         'is_english_primary_language': 'No', 'english_acquisition_age': 12, 'education_level': 6,
                         'income': 1, 'household_size': 9, 'ftnd_1': 1, 'ftnd_2': 1, 'ftnd_3': 1, 'ftnd_4': 1,
                         'ftnd_5': 1, 'ftnd_6': 1, 'distracted_level': 1, 'seriousness_level': 2,
                         'reframe_difficulty_level': 3, 'past_reframe_use': 'Never', 'current_smoking_frequency': 4,
                         'past_smoking_frequency': 3, 'past_daily_smoking': 'Unknown', 'messages': '',
                         'timestamp': '2020-05-26T09:23:51'}

        # Verify 200 OK is returned when a complete object is received
        with mock.patch('rethinksmoking.orm.mturk_worker.MturkWorker.add') as mock_add, \
                app.app_context():
            client = app.test_client()
            response = client.post('/worker', json=actual_worker, content_type='application/json')
            assert response.status_code == HTTPStatus.OK
            assert mock_add.called

    def test_success_with_messages(self, app):
        actual_worker = {'age': 10, 'gender': 'Female', 'is_hispanic': '2', 'ethnicity': 'Unknown',
                         'is_english_primary_language': 'Yes', 'english_acquisition_age': '', 'education_level': 7,
                         'income': 2, 'household_size': 10, 'ftnd_1': 1, 'ftnd_2': 1, 'ftnd_3': 1, 'ftnd_4': 1,
                         'ftnd_5': 1, 'ftnd_6': 1, 'distracted_level': 1, 'seriousness_level': 2,
                         'reframe_difficulty_level': 3, 'past_reframe_use': 'Never', 'current_smoking_frequency': 4,
                         'past_smoking_frequency': 3, 'past_daily_smoking': 'Unknown',
                         'messages': 'reframe 1\treframe 2', 'timestamp': '2020-05-26T09:23:51'}

        # Verify 200 OK is returned when a complete object is received
        with mock.patch('rethinksmoking.orm.mturk_worker.MturkWorker.add') as mock_add, \
                mock.patch('sqlalchemy.orm.collections.InstrumentedList.append') as mock_append, \
                app.app_context():
            client = app.test_client()
            response = client.post('/worker', json=actual_worker, content_type='application/json')
            assert response.status_code == HTTPStatus.OK
            assert mock_add.called
            assert mock_append.called
