#declaraçao das tabelas
from app import db

from sqlalchemy.ext.automap import automap_base


Base = automap_base()
Base.prepare(db.engine, reflect=True)
Transportadoras = Base.classes.transportadoras
Clientes = Base.classes.clientes
#Clientesenderecos = Base.classes.Clientesenderecos


#DECLARAÇÃO DO BANCO DE DADOS
class Transportadoras(db.Model):
    __tablename__ = "transportadoras"
    idtransportadora = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Transportadora = db.Column("transportadora", db.String)
    Cidade = db.Column("cidade", db.String)
    Estado = db.Column("estado",db.String)
    Telefone = db.Column("telefone", db.String)
    

class Clientes(db.Model):
    __tablename__ = "clientes"
    Idcliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Razao_social = db.Column(db.String(255))
    Nome_fantasia = db.Column( db.String(255))
    Cnpj = db.Column(db.String(255), unique=True, nullable=False)
    Inscricao_estadual = db.Column( db.String(255))
    Telefone = db.Column(db.String(255))
    Celular = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Danfe = db.Column(db.String(255))
    Site = db.Column(db.String(255))
    Vendedor = db.Column(db.String(255))
    Visita = db.Column(db.String(255))
    Observacoes = db. Column(db.String(255))
    Caixa_postal = db.Column(db.String(255))
    Status = db.Column(db.String(255))
    Pagamentos = db.Column(db.String(255))
    Enderecos = db.relationship('Clientesenderecos')
    

class Clientesenderecos(db.Model):
    __tablename__ = "clientesenderecos"
    idenderecos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    finalidade = db.Column("finalidade", db.String(255))
    endereco = db.Column('endereco', db.String(255))
    bairro = db.Column("bairro", db.String(255))
    cidade = db.Column('cidade', db.String(255))
    estado = db.Column('estado', db.String(255))
    cep = db.Column('cep', db.String(255))
    clienteid = db.Column(db.Integer, db.ForeignKey('clientes.idcliente'))




class Clientescontatos(db.Model):
    __tablename__ = "clientescontatos"
    idclientecontato = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    cargo = db.Column(db.String)
    telefone = db.Column(db.String)
    ramal = db.Column(db.String)
    celular = db.Column(db.String)
    email = db.Column(db.String)
    #idcliente = db.Column("Clientes",db.Integer, db.ForeignKey("clientes.Idcliente"), nullable=False)

