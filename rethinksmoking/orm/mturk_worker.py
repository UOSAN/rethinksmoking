from enum import Enum

from .database import db


class Gender(Enum):
    Male = 1
    Female = 2
    Transgender = 3
    Nonbinary = 4
    Other = 5


class IncomeLevel(Enum):
    Below25 = 1
    Between25to40 = 2
    Between40to75 = 3
    Between75to100 = 4
    Over100 = 5
    Unknown = 6
    DeclineToRespond = 7


class MturkWorker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Demographics
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum(Gender))
    race = db.Column(db.String)
    ethnicity = db.Column(db.String)
    english_primary_language = db.Column(db.Boolean)
    english_acquisition_age = db.Column(db.Integer)
    education_level = db.Column(db.String)
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
        return f'<MTurkWorker(id={self.id}, age={self.age}, gender={self.gender})>'

    def add(self):
        db.session.add(self)
        db.session.commit()
