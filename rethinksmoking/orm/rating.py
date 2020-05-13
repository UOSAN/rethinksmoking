from dataclasses import dataclass

from .database import db


@dataclass
class Rating(db.Model):
    id: int
    helpfulness: int
    relatability: int
    familiarity: int

    id = db.Column(db.Integer, primary_key=True)
    helpfulness = db.Column(db.Integer, nullable=False)
    relatability = db.Column(db.Integer, nullable=False)
    familiarity = db.Column(db.Integer, nullable=False)

    # Foreign key relationships with MturkWorker and Message tables
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', back_populates='ratings')

    rater_id = db.Column(db.Integer, db.ForeignKey('mturk_worker.id'), nullable=False)
    rater = db.relationship('MturkWorker', back_populates='rating')

    def add(self):
        db.session.add(self)
        db.session.commit()
