from flaskblog import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # Since user_id Column of User table is foreign key for Post table,
    # we can use post.author to access the owner / writer of the post.

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
