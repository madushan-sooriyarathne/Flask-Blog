from configparser import ConfigParser
import os

# you can also store these sensitive information in environment variables 
# and use os.environ['ENVIRONMENT_VARIABLE_YOU_WANT_TO_RETRIVE']

CONFIG_FILE = 'flaskblog/config.cfg'

if not os.path.exists(CONFIG_FILE):
    raise FileNotFoundError("Can't find the configurations file")

config = ConfigParser()
config.read(CONFIG_FILE)

class Config:
    MAIL_SERVER = config.get('FLASK_CONFIGS', 'MAIL_SERVER')
    MAIL_PORT = config.get('FLASK_CONFIGS', 'MAIL_PORT')
    MAIL_USE_TLS = True 
    MAIL_USERNAME = config.get('FLASK_CONFIGS', 'MAIL_USERNAME')
    MAIL_PASSWORD = config.get('FLASK_CONFIGS', 'MAIL_PASSWORD')
    SECRET_KEY = config.get('FLASK_CONFIGS', 'SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('FLASK_CONFIGS', 'DATABASE_URI')