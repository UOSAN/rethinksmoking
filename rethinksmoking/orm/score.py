from .database import db


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quality = db.Column(db.Integer, nullable=False)
    scorer_id = db.Column(db.String(length=1000), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', back_populates='scores')

    def __repr__(self):
        return f'<Score(quality={self.quality}, scorer={self.scorer_id})>'

    def add(self):
        db.session.add(self)
        db.session.commit()
