#declaraçao das tabelas
from app import db, app, SQLAlchemy

from sqlalchemy.ext.automap import automap_base


db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Transportadoras = Base.classes.transportadoras
Clientes = Base.classes.clientes


#DECLARAÇÃO DO BANCO DE DADOS
class Transportadoras(db.Model):
    __tablename__ = "transportadoras"
    idtransportadora = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Transportadora = db.Column(db.String)
    Cidade = db.Column(db.String)
    Estado = db.Column(db.String)
    Telefone = db.Column(db.String)
    