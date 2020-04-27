from .database import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_content = db.Column(db.String, nullable=False)
    condition = db.Column(db.String, nullable=False)

    # Foreign key relationship with MturkWorker table
    mturk_user_id = db.Column(db.Integer, db.ForeignKey('mturk_worker.id'), nullable=False)
    mturk_user = db.relationship('MturkWorker', back_populates='messages')

    def __repr__(self):
        return f'<Message(content={self.message_content})>'

    def add(self):
        db.session.add(self)
        db.session.commit()
