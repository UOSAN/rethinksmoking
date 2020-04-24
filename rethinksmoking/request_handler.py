from typing import Mapping, Union

from .orm.mturk_worker import MturkWorker


class RequestHandler:
    def __init__(self, request: Mapping[str, Union[str, bool, int]]):
        self._req = request

    def handle_request(self):
        worker = MturkWorker(age=self._req.get('age'), gender=self._req.get('gender'), race=self._req.get('race'),
                             ethnicity=self._req.get('ethnicity'),
                             english_primary_language=self._req.get('english_primary_language'),
                             education_level=self._req.get('education_level'), income=self._req.get('income'),
                             household_size=self._req.get('household_size'),
                             ftnd_1=self._req.get('ftnd_1'), ftnd_2=self._req.get('ftnd_2'),
                             ftnd_3=self._req.get('ftnd_3'), ftnd_4=self._req.get('ftnd_4'),
                             ftnd_5=self._req.get('ftnd_5'), ftnd_6=self._req.get('ftnd_6'))
        worker.add()
