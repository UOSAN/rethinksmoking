from typing import Mapping, Union

from .orm.message import Message
from .orm.mturk_worker import MturkWorker, IncomeLevel, EducationLevel


class RequestHandler:
    def __init__(self, request: Mapping[str, Union[str, bool, int]]):
        self._req = request

    def _get(self, key: str):
        return self._req.get(key)

    def handle_request(self):
        worker = MturkWorker(age=self._get('age'), gender=self._get('gender'),
                             is_hispanic=self._get('is_hispanic'), ethnicity=self._get('ethnicity'),
                             english_primary_language=self._get('english_primary_language'),
                             education_level=EducationLevel(int(self._get('education_level'))),
                             income=IncomeLevel(int(self._get('income'))),
                             household_size=self._get('household_size'),
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
