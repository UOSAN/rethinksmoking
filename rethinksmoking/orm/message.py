import json

from .enums import Condition
from .database import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_content = db.Column(db.String(length=1000), nullable=False)
    condition = db.Column(db.Enum(Condition), nullable=False)

    # Foreign key relationship with MturkWorker table
    mturk_user_id = db.Column(db.Integer, db.ForeignKey('mturk_worker.id'), nullable=False)
    mturk_user = db.relationship('MturkWorker', back_populates='messages')

    scores = db.relationship('Score', back_populates='message')

    ratings = db.relationship('Rating', back_populates='message')

    def __repr__(self):
        return json.dumps(self, cls=MessageEncoder)

    def add(self):
        db.session.add(self)
        db.session.commit()


class MessageEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Message):
            return {
                "id": o.id,
                "message_content": o.message_content,
                "condition": str(o.condition)
            }
        return json.JSONEncoder.default(self, o)
