from enum import Enum


class Gender(Enum):
    Male = 1
    Female = 2
    Transgender = 3
    Nonbinary = 4
    Other = 5

    def __str__(self):
        gender_to_string = {
            Gender.Male: 'Male',
            Gender.Female: 'Female',
            Gender.Transgender: 'Transgender',
            Gender.Nonbinary: 'Nonbinary',
            Gender.Other: 'Other'
        }
        return gender_to_string[self]


class IncomeLevel(Enum):
    Below25 = 1
    Between25to40 = 2
    Between40to75 = 3
    Between75to100 = 4
    Over100 = 5
    Unknown = 6
    DeclineToRespond = 7

    def __str__(self):
        income_to_string = {
            IncomeLevel.Below25: 'Up to $25,000',
            IncomeLevel.Between25to40: '$25,000 - $40,000',
            IncomeLevel.Between40to75: '$40,000 - $75,000',
            IncomeLevel.Between75to100: '$75,000 - $100,000',
            IncomeLevel.Over100: 'Over $100,000',
            IncomeLevel.Unknown: 'Unknown',
            IncomeLevel.DeclineToRespond: 'Decline to respond'
        }
        return income_to_string[self]


class EducationLevel(Enum):
    NoSchooling = 1
    Grades1Through11 = 2
    HighSchoolNoDiploma = 3
    HighSchoolDiploma = 4
    GED = 5
    LessThanOneYearCollege = 6
    MoreThanOneYearCollege = 7
    AssociateDegree = 8
    BachelorsDegree = 9
    MastersDegree = 10
    ProfessionalDegree = 11
    DoctorateDegree = 12

    def __str__(self):
        education_to_string = {
            EducationLevel.NoSchooling: 'No schooling completed',
            EducationLevel.Grades1Through11: 'Grades 1 through 11',
            EducationLevel.HighSchoolNoDiploma: '12th grade - no diploma',
            EducationLevel.HighSchoolDiploma: 'Regular high school diploma',
            EducationLevel.GED: 'GED or alternative credential',
            EducationLevel.LessThanOneYearCollege: 'Some college credit, but less than 1 year of college',
            EducationLevel.MoreThanOneYearCollege: '1 or more years of college credit, no degree',
            EducationLevel.AssociateDegree: 'Associate degree',
            EducationLevel.BachelorsDegree: 'Bachelor\'s degree',
            EducationLevel.MastersDegree: 'Master\'s degree',
            EducationLevel.ProfessionalDegree: 'Professional degree beyond bachelors degree',
            EducationLevel.DoctorateDegree: 'Doctorate degree'
        }

        return education_to_string[self]


class SmokingFrequency(Enum):
    Daily = 1
    LessThanDaily = 2
    NotAtAll = 3
    Unknown = 4

    def __str__(self):
        smoking_frequency_to_string = {
            SmokingFrequency.Daily: 'Daily',
            SmokingFrequency.LessThanDaily: 'Less than daily',
            SmokingFrequency.NotAtAll: 'Not at all',
            SmokingFrequency.Unknown: 'Don\'t know'
        }
        return smoking_frequency_to_string[self]


class FivePointScale(Enum):
    NotAtAll = 1
    ALittle = 2
    Somewhat = 3
    Very = 4
    Extremely = 5

    def __str__(self):
        scale_to_string = {
            FivePointScale.NotAtAll: 'Not at all',
            FivePointScale.ALittle: 'A little',
            FivePointScale.Somewhat: 'Somewhat',
            FivePointScale.Very: 'Very',
            FivePointScale.Extremely: 'Extremely'
        }
        return scale_to_string[self]


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
