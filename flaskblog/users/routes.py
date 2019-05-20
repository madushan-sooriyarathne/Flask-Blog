from flask import render_template, url_for, flash, redirect, request, Blueprint
from flaskblog import db, bcrypt
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, PasswordResetEmailForm, PasswordResetForm
from flaskblog.users.models import User
from flaskblog.posts.models import Post
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog.users.utils import save_picture, remove_picure, reset_email


# initiating the Blueprint Object
users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
	# if user is already loged in and authenticated they will redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
        
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
        	# if a user exists with that email and their pasword hashes match, they will be loge in via flask_login's login_user function
            login_user(user, remember=form.remember.data)

			# if user got redirect to login route from some other route 
			# (if user tried to visit a route that is login required, flask will redirect them to login route) 
			# url parameter called 'next' will be added to url. it will contain the previous rotute that user came from
			# and when they successfuly loged in, they will redirected back to the route that they came
			# if there's no parameter called next in the url, they will redirect to home route
            next_page = request.args.get('next')
            if next_page:
                flash(f"Login successful!", "success")
                return redirect(next_page)
            else:
                flash(f"Login successful!", "success")
                return redirect(url_for('main.home'))
        else:
            flash(f"Login unsuccessful! Please check your email & password", "danger")
        
    return render_template('login.html', title='Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
    

@users.route('/register', methods=['GET', 'POST'])
def register():
	# if user is already loged in and authenticated they will redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
    
    	# hashing the password that user enterd
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        # creting the user with given details and hashed password
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        
        # adding user to db and commiting changes
        db.session.add(user)
        db.session.commit()
        
        flash(f"Account has been created! you are now able to log in", "success")
        return redirect(url_for('users.login'))

    return render_template('register.html', title='Register Now', form=form)


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            file_name = save_picture(form.picture.data)
            remove_picure(current_user.image_file)
            # updating the image file 
            current_user.image_file = file_name
        
        # Updating the user details with given values
        current_user.username = form.username.data
        current_user.email = form.email.data
        
        # commiting all changes 
        db.session.commit()
        
        flash('Your account information has been updated succesfully', 'success')
        return redirect(url_for('users.account'))
        
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title="Account", image=image, form=form)

@users.route('/user/<string:username>', methods=['GET'])
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404() # return 404 not found page if user not found for given username
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted).paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = PasswordResetEmailForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        reset_email(user)
        flash(f'Password Reqeust Email has been sent to {form.email.data}. Please check your inbox', 'success')
        return redirect(url_for('users.login'))

    return render_template('password_reset_request.html', title='Reset Password', form=form)

@users.route('/reset_password/<string:token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_auth_token(token)
    if user is None:
        flash('Invalid or Expired token', 'danger')
        return redirect(url_for('users.reset_request'))

    form = PasswordResetForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pw
        db.session.commit()
        flash(f'Your Password has been updated. Now you can login', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_password.html', title='Update Password', form=form)
