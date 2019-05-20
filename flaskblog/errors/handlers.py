from flask import Blueprint
from flask import render_template

errors = Blueprint('errors', __name__)

# It's not .route() Keep that in mind
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_404(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_404(error):
    return render_template('errors/500.html'), 500