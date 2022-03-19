from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite///base.db'
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{root}:{}@{localhost}/testadb".format(username, password, server)
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@server/db"

#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.config['secret_key'] = 'frase_secreta'

from app.controllers import default





