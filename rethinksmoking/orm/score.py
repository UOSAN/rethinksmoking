from dataclasses import dataclass

from .database import db


@dataclass
class Score(db.Model):
    id: int
    quality: int
    scorer_id: str

    id = db.Column(db.Integer, primary_key=True)
    quality = db.Column(db.Integer, nullable=False)
    scorer_id = db.Column(db.String(length=1000), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', back_populates='scores')

    def add(self):
        db.session.add(self)
        db.session.commit()
