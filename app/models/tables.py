#declaraçao das tabelas
from app import db

from sqlalchemy.ext.automap import automap_base



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
    