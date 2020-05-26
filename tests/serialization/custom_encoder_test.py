import json

from rethinksmoking.custom_encoder import CustomEncoder
from rethinksmoking.orm.enums import Gender, EducationLevel, IncomeLevel, SmokingFrequency, FivePointScale, Condition


class TestCustomEncoder:
    def test_json_encoding(self):
        g = Gender.Nonbinary
        s = json.dumps(g, cls=CustomEncoder)
        assert s == f'\"{str(g)}\"'

        e = EducationLevel.BachelorsDegree
        s = json.dumps(e, cls=CustomEncoder)
        assert s == f'\"{str(e)}\"'

        i = IncomeLevel.Between40to75
        s = json.dumps(i, cls=CustomEncoder)
        assert s == f'\"{str(i)}\"'

        sf = SmokingFrequency.LessThanDaily
        s = json.dumps(sf, cls=CustomEncoder)
        assert s == f'\"{str(sf)}\"'

        f = FivePointScale.NotAtAll
        s = json.dumps(f, cls=CustomEncoder)
        assert s == f'\"{str(f)}\"'

        c = Condition.DownRegulation
        s = json.dumps(c, cls=CustomEncoder)
        assert s == f'\"{str(c)}\"'

