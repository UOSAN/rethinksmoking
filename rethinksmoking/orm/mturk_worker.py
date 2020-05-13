from dataclasses import dataclass
from typing import List

from .database import db
from .enums import Gender, EducationLevel, FivePointScale, IncomeLevel, SmokingFrequency
from .message import Message


@dataclass
class MturkWorker(db.Model):
    id: int
    age: int
    gender: Gender
    is_hispanic: bool
    ethnicity: str
    is_english_primary_language: bool
    english_acquisition_age: int
    education_level: EducationLevel
    income: IncomeLevel
    household_size: int
    distracted_level: FivePointScale
    seriousness_level: FivePointScale
    reframe_difficulty_level: FivePointScale
    past_reframe_use: str
    current_smoking_frequency: SmokingFrequency
    past_smoking_frequency: SmokingFrequency
    past_daily_smoking: str
    ftnd_1: int
    ftnd_2: int
    ftnd_3: int
    ftnd_4: int
    ftnd_5: int
    ftnd_6: int
    messages: List[Message]

    id = db.Column(db.Integer, primary_key=True)
    # Demographics
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum(Gender))
    is_hispanic = db.Column(db.Boolean)
    ethnicity = db.Column(db.String(300))
    is_english_primary_language = db.Column(db.Boolean)
    english_acquisition_age = db.Column(db.Integer)
    education_level = db.Column(db.Enum(EducationLevel))
    income = db.Column(db.Enum(IncomeLevel))
    household_size = db.Column(db.Integer)

    # Engagement in survey
    distracted_level = db.Column(db.Enum(FivePointScale))
    seriousness_level = db.Column(db.Enum(FivePointScale))
    reframe_difficulty_level = db.Column(db.Enum(FivePointScale))
    past_reframe_use = db.Column(db.String(50))

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

    def add(self):
        db.session.add(self)
        db.session.commit()
