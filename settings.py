import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('sqlite:///db.sqlite3')
    SECRET_KEY = os.getenv('MY_SECRET_KEY')