import os

# App config
SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
APP_PATH = os.path.dirname(os.path.abspath(__file__))

# Database
if os.getenv("FLASK_ENV") == "development":
    SQLALCHEMY_DATABASE_URI = 'sqlite:///base.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

else:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/testadb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
