import json

from .database import db


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    helpfulness = db.Column(db.Integer, nullable=False)
    relatability = db.Column(db.Integer, nullable=False)
    familiarity = db.Column(db.Integer, nullable=False)

    # Foreign key relationships with MturkWorker and Message tables
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', back_populates='ratings')

    rater_id = db.Column(db.Integer, db.ForeignKey('mturk_worker.id'), nullable=False)
    rater = db.relationship('MturkWorker', back_populates='rating')

    def __repr__(self):
        return json.dumps(self, cls=RatingEncoder)

    def add(self):
        db.session.add(self)
        db.session.commit()


class RatingEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Rating):
            return {
                "id": o.id,
                "helpfulness": o.helpfulness,
                "condition": o.relatability,
                "familiarity": o.familiarity
            }
        return json.JSONEncoder.default(self, o)
