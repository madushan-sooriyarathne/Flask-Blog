from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flaskblog import db
from flaskblog.posts.forms import PostForm, EditPostForm
from flaskblog.posts.models import Post
from flask_login import current_user, login_required


posts = Blueprint('posts', __name__)

@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('You post successfuly created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form)


@posts.route('/post/<int:post_id>', methods=['GET'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    # get_or_404 : if sqlalchemy can't find a post with given post_id it will retrun a 404 not found error page
    return render_template('post.html', title=post.title, post=post)

@posts.route('/post/<int:post_id>/edit/', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = EditPostForm()

    if current_user != post.author:
        return abort(403)
        # if a user tries to edit a post from another user it will abort the connection with 404 (forbidden) error
        
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.title.data
        db.session.commit()
        flash('You post successfuly Updated!', 'success')
        return redirect(url_for('main.home'))
    form.title.data = post.title
    form.content.data = post.content
    return render_template('edit_post.html', title='Edit Post', form=form)
    
@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if current_user != post.author:
        return abort(403)
    
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted successfuly!', 'success')
    return redirect(url_for('main.home'))

