from datetime import datetime

from rethinksmoking.orm.message import Message
from rethinksmoking.orm.enums import FivePointScale, Gender, IncomeLevel, EducationLevel
from rethinksmoking.orm.mturk_worker import MturkWorker


class TestMturkWorker:
    def test_post_mturk_worker(self, session):
        expected_age = 10
        user = MturkWorker(age=expected_age, gender=Gender.Female, is_hispanic=True, ethnicity='Unknown',
                           is_english_primary_language=True, english_acquisition_age=10,
                           education_level=EducationLevel.NoSchooling, income=IncomeLevel.Below25, household_size=9,
                           distracted_level=FivePointScale.NotAtAll, seriousness_level=FivePointScale.Extremely,
                           ftnd_1=1, ftnd_2=1, ftnd_3=1, ftnd_4=1, ftnd_5=1, ftnd_6=1)
        user.add()

        actual_count = MturkWorker.query.count()
        assert actual_count == 1

        actual_user = MturkWorker.query.limit(1).first()
        assert actual_user.age == expected_age

        assert len(actual_user.messages) == 0

    def test_post_mturk_worker_with_messages(self, session):
        expected_age = 10
        expected_content = 'Test message'
        user = MturkWorker(age=expected_age, gender=Gender.Transgender, is_hispanic=False,
                           ethnicity='Unknown', is_english_primary_language=True, english_acquisition_age=10,
                           education_level=EducationLevel.GED, income=IncomeLevel.Between25to40, household_size=9,
                           distracted_level=FivePointScale.Very, seriousness_level=FivePointScale.ALittle,
                           ftnd_1=1, ftnd_2=1, ftnd_3=1, ftnd_4=1, ftnd_5=1, ftnd_6=1)
        user.messages.append(Message(message_content=expected_content, condition='SelfAffirmation',
                                     timestamp=datetime.now()))
        user.add()

        actual_count = MturkWorker.query.count()
        assert actual_count == 1

        actual_user = MturkWorker.query.limit(1).first()
        assert actual_user.age == expected_age

        assert len(actual_user.messages) == 1
        assert actual_user.messages[0].message_content == expected_content
