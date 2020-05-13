from flask.json import JSONEncoder

from .orm.enums import Gender, EducationLevel, IncomeLevel, SmokingFrequency, FivePointScale, Condition


class CustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Gender) or isinstance(o, EducationLevel) or isinstance(o, IncomeLevel) or \
                isinstance(o, SmokingFrequency) or isinstance(o, FivePointScale) or isinstance(o, Condition):
            return str(o)
        return JSONEncoder.default(self, o)
