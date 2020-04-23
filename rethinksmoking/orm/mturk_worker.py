from .database import db


class MturkWorker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    race = db.Column(db.String)
    ethnicity = db.Column(db.String)
    english_primary_language = db.Column(db.Boolean)
    education_level = db.Column(db.String)
    income = db.Column(db.String)
    household_size = db.Column(db.Integer)

    # Fagerström Test for Nicotine Dependence
    ftnd_1 = db.Column(db.Integer)  # How soon after you wake up do you smoke your first cigarette?
    ftnd_2 = db.Column(db.Integer)  # Do you find it difficult to refrain from smoking in places where it is forbidden?
    ftnd_3 = db.Column(db.Integer)  # Which cigarette would you hate most to give up?
    ftnd_4 = db.Column(db.Integer)  # How many cigarettes per day do you smoke?
    ftnd_5 = db.Column(db.Integer)  # Do you smoke more in the first hours after waking than during the rest of the day?
    ftnd_6 = db.Column(db.Integer)  # Do you smoke even when you are ill enough to be in bed most of the day?

    def __repr__(self):
        return f'<MTurkWorker(id={self.id}, age={self.age}, gender={self.gender})>'


def add_worker(worker: MturkWorker):
    db.session.add(worker)
    db.session.commit()
