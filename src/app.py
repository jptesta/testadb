import os
from database import db
from flask import Flask
from flask_migrate import Migrate
from controllers.default import bp_default
from controllers.transportadoras import bp_transportadoras
from controllers.representadas import bp_representadas

app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(bp_default)
app.register_blueprint(bp_transportadoras)
app.register_blueprint(bp_representadas)

