import json

from .database import db
from .enums import Gender, EducationLevel, IncomeLevel, SmokingFrequency


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
    reframe_difficulty_level = db.Column(db.Integer)
    past_reframe_use = db.Column(db.Integer)

    # Smoking level
    current_smoking_frequency = db.Column(db.Enum(SmokingFrequency))
    past_smoking_frequency = db.Column(db.Enum(SmokingFrequency))
    past_daily_smoking = db.Column(db.String(15))

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
                "current_smoking_frequency": str(o.current_smoking_frequency),
                "past_smoking_frequency": str(o.past_smoking_frequency),
                "past_daily_smoking": o.past_daily_smoking,
                "ftnd_1": o.ftnd_1,
                "ftnd_2": o.ftnd_2,
                "ftnd_3": o.ftnd_3,
                "ftnd_4": o.ftnd_4,
                "ftnd_5": o.ftnd_5,
                "ftnd_6": o.ftnd_6
            }
        return json.JSONEncoder.default(self, o)
