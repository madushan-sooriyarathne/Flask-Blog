from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
from flaskblog import db, login_manager
from flask_login import UserMixin
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='defualt.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


    
    def generate_token(self, expire_time=3600):
        # generate a timed token using project secret key. 
        serializer = Serializer(current_app.config['SECRET_KEY'], expires_in=expire_time)
        return serializer.dumps({'user_id': self.id}) # return the generetated token

    @staticmethod
    def verify_auth_token(token):
        serializer = Serializer(current_app.config['SECRET_KEY'])

        # if token is invalid or expired return None
        try:
            data = serializer.loads(token)
        except BadSignature as bad_token:
            return None
        except SignatureExpired as expired_token:
            return None
        
        return User.query.get(data['user_id'])