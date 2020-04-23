def test_add_worker_and_messages_bad_request(app):
    # Verify that 400 Bad Request is returned on a bad request
    with app.app_context():
        client = app.test_client()
        response = client.post('/worker/message', data='some garbage test data', content_type='application/text')
        assert response.status == '400 BAD REQUEST'
