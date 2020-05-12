from rethinksmoking.orm.enums import Gender, IncomeLevel, EducationLevel, SmokingFrequency, FivePointScale, Condition


def test_gender_str():
    expected = 'Other'
    actual = str(Gender.Other)

    assert expected == actual


def test_income_level_str():
    expected = '$75,000 - $100,000'
    actual = str(IncomeLevel.Between75to100)

    assert expected == actual


def test_education_level_str():
    expected = 'Bachelor\'s degree'
    actual = str(EducationLevel.BachelorsDegree)

    assert expected == actual


def test_smoking_frequency_str():
    expected = 'Less than daily'
    actual = str(SmokingFrequency.LessThanDaily)

    assert expected == actual


def test_five_point_scale_str():
    expected = 'Not at all'
    actual = str(FivePointScale.NotAtAll)

    assert expected == actual


def test_condition_str():
    expected = 'DownRegulation'
    actual = str(Condition.DownRegulation)

    assert expected == actual
