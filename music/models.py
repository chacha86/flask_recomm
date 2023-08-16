from music import db

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, nullable=False)
    artistid = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)