import os
from database import db
from flask import Flask
from flask_migrate import Migrate
from controllers.default import bp_default

app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(bp_default)
