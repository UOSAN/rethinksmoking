from datetime import datetime

from rethinksmoking.orm.message import Message
from rethinksmoking.orm.score import Score
from rethinksmoking.orm.rating import Rating


class TestMessage:
    def test_post_message(self, session):
        expected_content = 'test content'
        expected_condition = 'ConstrualLevel'

        message = Message(message_content=expected_content, condition=expected_condition, timestamp=datetime.now(), mturk_user_id=1)
        message.add()

        # Verify only message in database has correct content
        actual_count = Message.query.count()
        assert actual_count == 1

        actual_message = Message.query.limit(1).first()
        assert actual_message.message_content == expected_content

    def test_post_multiple_messages(self, session):
        expected_content = 'test content'
        expected_condition = 'ConstrualLevel'

        message1 = Message(message_content=expected_content, condition=expected_condition, timestamp=datetime.now(), mturk_user_id=1)
        message1.add()

        message2 = Message(message_content=expected_content, condition=expected_condition, timestamp=datetime.now(), mturk_user_id=1)
        message2.add()

        # Verify correct number of messages
        actual_count = Message.query.count()
        assert actual_count == 2

    def test_post_message_with_scores(self, session):
        expected_content = 'test content'
        expected_condition = 'DownRegulation'

        message = Message(message_content=expected_content, condition=expected_condition, timestamp=datetime.now(), mturk_user_id=1)
        message.scores.append(Score(quality=2, scorer_id='JM'))
        message.add()

        # Verify only message in database has scores
        actual_message = Message.query.limit(1).first()
        assert len(actual_message.scores) == 1
        assert actual_message.scores[0].quality == 2

    def test_post_message_with_ratings(self, session):
        expected_content = 'test content'
        expected_condition = 'DownRegulation'

        message = Message(message_content=expected_content, condition=expected_condition, timestamp=datetime.now(),  mturk_user_id=1)
        message.ratings.append(Rating(helpfulness=2, relatability=1, familiarity=3, rater_id=1))
        message.add()

        # Verify only message in database has scores
        actual_message = Message.query.limit(1).first()
        assert len(actual_message.ratings) == 1
        assert actual_message.ratings[0].helpfulness == 2