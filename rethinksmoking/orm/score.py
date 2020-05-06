import json

from .database import db


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quality = db.Column(db.Integer, nullable=False)
    scorer_id = db.Column(db.String(length=1000), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', back_populates='scores')

    def __repr__(self):
        return json.dumps(self, cls=ScoreEncoder)

    def add(self):
        db.session.add(self)
        db.session.commit()


class ScoreEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Score):
            return {
                "id": o.id,
                "quality": o.quality,
                "scorer_id": o.scorer_id,
                "message_id": o.message_id,
                "message": o.message
            }
        return json.JSONEncoder.default(self, o)
