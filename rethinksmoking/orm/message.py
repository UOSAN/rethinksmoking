from dataclasses import dataclass
from typing import List

from .enums import Condition
from .database import db
from .score import Score
from .rating import Rating


@dataclass
class Message(db.Model):
    id: int
    message_content: str
    condition: Condition
    scores: List[Score]
    ratings: List[Rating]

    id = db.Column(db.Integer, primary_key=True)
    message_content = db.Column(db.String(length=1000), nullable=False)
    condition = db.Column(db.Enum(Condition), nullable=False)

    # Foreign key relationship with MturkWorker table
    mturk_user_id = db.Column(db.Integer, db.ForeignKey('mturk_worker.id'), nullable=False)
    mturk_user = db.relationship('MturkWorker', back_populates='messages')

    scores = db.relationship('Score', back_populates='message')

    ratings = db.relationship('Rating', back_populates='message')

    def add(self):
        db.session.add(self)
        db.session.commit()
