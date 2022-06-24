#declaraçao das tabelas

from app import db

from sqlalchemy.ext.automap import automap_base




Base = automap_base()
Base.prepare(db.engine, reflect=True)
#Transportadoras = Base.classes.transportadoras
#Clientes = Base.classes.clientes
#Clientesenderecos = Base.classes.clientesenderecos

print(dir(Base.classes))

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
    Enderecos = db.relationship('Clientesenderecos', backref="cliend")
    Contatos = db.relationship('Clientescontatos', backref="clicon")
    Contatosrealizados = db.relationship('Contatos_realizados', backref="crealizado")
    

class Clientesenderecos(db.Model):
    __tablename__ = "clientesenderecos"
    Idclientesenderecos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Finalidade = db.Column("finalidade", db.String(255))
    Endereco = db.Column('endereco', db.String(255))
    Bairro = db.Column("bairro", db.String(255))
    Cidade = db.Column('cidade', db.String(255))
    Estado = db.Column('estado', db.String(255))
    Cep = db.Column('cep', db.String(255))
    idcliente = db.Column(db.Integer, db.ForeignKey('clientes.Idcliente'))
    

class Clientescontatos(db.Model):
    __tablename__ = "clientescontatos"
    Idclientecontato = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nome = db.Column(db.String)
    Cargo = db.Column(db.String)
    Telefone = db.Column(db.String)
    Ramal = db.Column(db.String)
    Celular = db.Column(db.String)
    Email = db.Column(db.String)
    idcliente = db.Column(db.Integer, db.ForeignKey("clientes.Idcliente"))

class Representadas(db.Model):
    __tablename__ = "representadas"
    Idrepresentada = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Razaosocial = db.Column(db.String)
    Cnpj=db.Column(db.String)
    Inscricaoestadual = db.Column(db.String)
    Telefone = db.Column(db.String)
    Endereco = db.Column(db.String)
    Bairro = db.Column(db.String)
    Cidade = db.Column(db.String)
    Estado = db.Column(db.String)
    Cep = db.Column(db.String)
    Comissao = db.Column(db.String)
    Contatos = db.relationship("Representadascontatos", backref="rcontato")

class Representadascontatos(db.Model):
    __tablename__= "representadascontatos"
    Idcontatorepresentada = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nome = db.Column(db.String)
    Cargo = db.Column(db.String)
    Telefone = db.Column(db.String)
    Celular = db.Column(db.String)
    Email = db.Column(db.String)
   # Representada = db.relationship("representa", backref="repre")
    Idrepresentada = db.Column(db.Integer, db.ForeignKey("representadas.Idrepresentada"))

class Contatos_realizados(db.Model):
    __tablename__ = "contatos_realizados"
    Id_contato_realizados = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Data_contato = db.Column(db.String)
    #Idcliente = db.Column(db.String)
    Pessoa_de_contato = db.Column(db.String)
    Metodo_de_contato = db.Column(db.String)
    Descricao = db.Column(db.String)
    idcliente = db.Column(db.Integer, db.ForeignKey("clientes.Idcliente"))

