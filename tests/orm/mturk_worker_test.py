from rethinksmoking.orm.mturk_worker import MturkWorker
from rethinksmoking.orm.message import Message


class TestMturkWorker:
    def test_post_mturk_worker(self, session):
        expected_age = 10
        user = MturkWorker(age=expected_age, gender='Female', race='Hispanic and/or Latinx', ethnicity='Unknown',
                           english_primary_language=True, education_level='No schooling completed',
                           income='25000', household_size=9, ftnd_1=1, ftnd_2=1, ftnd_3=1, ftnd_4=1,
                           ftnd_5=1, ftnd_6=1, messages=[])
        user.add()

        actual_count = MturkWorker.query.count()
        assert actual_count == 1

        actual_user = MturkWorker.query.limit(1).first()
        assert actual_user.age == expected_age

        assert len(actual_user.messages) == 0

    def test_post_mturk_worker_with_messages(self, session):
        expected_age = 10
        expected_content = 'Test message'
        user = MturkWorker(age=expected_age, gender='Female', race='Hispanic and/or Latinx', ethnicity='Unknown',
                           english_primary_language=True, education_level='No schooling completed',
                           income='25000', household_size=9, ftnd_1=1, ftnd_2=1, ftnd_3=1, ftnd_4=1,
                           ftnd_5=1, ftnd_6=1)
        user.messages.append(Message(message_content=expected_content, condition='Unknown'))
        user.add()

        actual_count = MturkWorker.query.count()
        assert actual_count == 1

        actual_user = MturkWorker.query.limit(1).first()
        assert actual_user.age == expected_age

        assert len(actual_user.messages) == 1
        assert actual_user.messages[0].message_content == expected_content
