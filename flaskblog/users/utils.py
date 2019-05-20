import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flaskblog import mail
from flask_mail import Message


# Save image file into disk
def save_picture(image):
    random_hex = secrets.token_hex(8) # Generate a random hex value for file name of image
    _, file_ext = os.path.splitext(image.filename)
    picture_fn = random_hex + file_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    # Resize the picture before saving
    output_size = (125, 125)
    i = Image.open(image)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# remove prvious picture
def remove_picure(file_name):
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', file_name)
    os.remove(picture_path)

def reset_email(user):
    token = user.generate_token()
    msg = Message('Password Reset Request', sender='noreply@madushan.me', recipients=[user.email])

    msg.body = f'''To reset your password, Vist Following Link
{url_for('users.reset_token', token=token, _external=True)}

If you didn't make this request, then simply ignore this email and no changes will be made
    '''
    # genereate the token and send an email with the password reset link
    mail.send(msg)
    
