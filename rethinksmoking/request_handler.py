from typing import Mapping, Union

from .orm.message import Message
from .orm.mturk_worker import MturkWorker, IncomeLevel, EducationLevel, FivePointScale, SmokingFrequency
from .orm.score import Score


class RequestHandler:
    def __init__(self, request: Mapping[str, Union[str, bool, int]]):
        self._req = request

    def _get(self, key: str):
        return self._req[key]

    def _get_bool(self, key: str):
        if key == 'is_hispanic':
            return self._get(key) == '1'
        elif key == 'is_english_primary_language':
            return self._get(key) == 'Yes'
        else:
            return self._req[key]

    def handle_request(self):
        worker = MturkWorker(age=self._get('age'), gender=self._get('gender'),
                             is_hispanic=self._get_bool('is_hispanic'), ethnicity=self._get('ethnicity'),
                             is_english_primary_language=self._get_bool('is_english_primary_language'),
                             english_acquisition_age=self._get('english_acquisition_age'),
                             education_level=EducationLevel(int(self._get('education_level'))),
                             income=IncomeLevel(int(self._get('income'))),
                             household_size=self._get('household_size'),
                             distracted_level=FivePointScale(int(self._get('distracted_level'))),
                             seriousness_level=FivePointScale(int(self._get('seriousness_level'))),
                             reframe_difficulty_level=FivePointScale(int(self._get('reframe_difficulty_level'))),
                             past_reframe_use=self._get('past_reframe_use'),
                             current_smoking_frequency=SmokingFrequency(int(self._get('current_smoking_frequency'))),
                             past_smoking_frequency=SmokingFrequency(int(self._get('past_smoking_frequency'))),
                             past_daily_smoking=self._get('past_daily_smoking'),
                             ftnd_1=self._get('ftnd_1'), ftnd_2=self._get('ftnd_2'),
                             ftnd_3=self._get('ftnd_3'), ftnd_4=self._get('ftnd_4'),
                             ftnd_5=self._get('ftnd_5'), ftnd_6=self._get('ftnd_6'))
        # messages is a field of tab-separated values. Do not create database entries for empty strings.
        messages = (self._get('messages') or '').split('\t')
        for m in messages:
            if len(m) > 0:
                message = Message(message_content=m, condition='DownRegulation')
                worker.messages.append(message)

        worker.add()

    def post_score(self):
        message_id = self._get('message_id')
        message = Message.query.get(message_id)

        score = Score(quality=self._get('quality'), scorer_id=self._get('scorer_id'))
        message.scores.append(score)
        score.add()
