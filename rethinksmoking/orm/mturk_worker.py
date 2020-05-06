import json
from enum import Enum

from .database import db


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
    AssociatesDegree = 8
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
            EducationLevel.AssociatesDegree: 'Associates degree',
            EducationLevel.BachelorsDegree: 'Bachelors degree',
            EducationLevel.MastersDegree: 'Masters degree',
            EducationLevel.ProfessionalDegree: 'Professional degree beyond bachelors degree',
            EducationLevel.DoctorateDegree: 'Doctorate degree'
        }

        return education_to_string[self]


class MturkWorker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Demographics
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum(Gender))
    is_hispanic = db.Column(db.Boolean)
    ethnicity = db.Column(db.String(300))
    english_primary_language = db.Column(db.Boolean)
    english_acquisition_age = db.Column(db.Integer)
    education_level = db.Column(db.Enum(EducationLevel))
    income = db.Column(db.Enum(IncomeLevel))
    household_size = db.Column(db.Integer)

    # Engagement in survey
    distracted_level = db.Column(db.Integer)
    seriousness_level = db.Column(db.Integer)

    # Fagerström Test for Nicotine Dependence
    ftnd_1 = db.Column(db.Integer)  # How soon after you wake up do you smoke your first cigarette?
    ftnd_2 = db.Column(db.Integer)  # Do you find it difficult to refrain from smoking in places where it is forbidden?
    ftnd_3 = db.Column(db.Integer)  # Which cigarette would you hate most to give up?
    ftnd_4 = db.Column(db.Integer)  # How many cigarettes per day do you smoke?
    ftnd_5 = db.Column(db.Integer)  # Do you smoke more in the first hours after waking than during the rest of the day?
    ftnd_6 = db.Column(db.Integer)  # Do you smoke even when you are ill enough to be in bed most of the day?

    messages = db.relationship('Message', back_populates='mturk_user')

    rating = db.relationship('Rating', back_populates='rater')

    def __repr__(self):
        return json.dumps(self, cls=MturkWorkerEncoder)

    def add(self):
        db.session.add(self)
        db.session.commit()


class MturkWorkerEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, MturkWorker):
            return {
                "id": o.id,
                "age": o.age,
                "gender": str(o.gender),
                "is_hispanic": o.is_hispanic,
                "ethnicity": o.ethnicity,
                "english_primary_language": o.english_primary_language,
                "english_acquisition_age": o.english_acquisition_age,
                "education_level": str(o.education_level),
                "income": str(o.income),
                "household_size": o.household_size,
                "ftnd_1": o.ftnd_1,
                "ftnd_2": o.ftnd_2,
                "ftnd_3": o.ftnd_3,
                "ftnd_4": o.ftnd_4,
                "ftnd_5": o.ftnd_5,
                "ftnd_6": o.ftnd_6
            }
        return json.JSONEncoder.default(self, o)
