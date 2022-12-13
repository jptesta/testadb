from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite///base.db'
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{root}:{}@{localhost}/testadb".format(username, password, server)
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@server/db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/testadb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.secret_key = 'secret@@@##$)(*&¨%$#@' 

db = SQLAlchemy(app)

from app.controllers import default






