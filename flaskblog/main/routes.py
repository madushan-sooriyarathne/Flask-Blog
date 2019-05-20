from flask import request, render_template, Blueprint
from flaskblog.posts.models import Post

main = Blueprint('main', __name__)

@main.route('/')
def home():
    page = request.args.get('page', 1, type=int) # Get the url atribute named 'page'(type int) if not found default will use. 
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5) # get the posts ordered by date. in descending order
    return render_template('home.html', posts=posts)

@main.route('/about')
def about():
    # TODO finish this route by adding a html template
    return render_template('about.html')