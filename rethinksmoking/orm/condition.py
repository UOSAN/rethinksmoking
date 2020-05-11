from enum import Enum


class Condition(Enum):
    DownRegulation = 1
    ConstrualLevel = 2
    SelfAffirmation = 3

    def __str__(self):
        condition_to_string = {
            Condition.DownRegulation: 'DownRegulation',
            Condition.ConstrualLevel: 'ConstrualLevel',
            Condition.SelfAffirmation: 'SelfAffirmation'
        }
        return condition_to_string[self]