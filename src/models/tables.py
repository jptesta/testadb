# declaraçao das tabelas

from database import db

class Clientes(db.Model):
    __tablename__ = "clientes"
    Idcliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Razao_social = db.Column(db.String(255))
    Nome_fantasia = db.Column(db.String(255))
    Cnpj = db.Column(db.String(255), unique=True, nullable=False)
    Inscricao_estadual = db.Column(db.String(255))
    Telefone = db.Column(db.String(255))
    Celular = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Danfe = db.Column(db.String(255))
    Site = db.Column(db.String(255))
    Vendedor = db.Column(db.String(255))
    Visita = db.Column(db.String(255))
    Observacoes = db.Column(db.String(255))
    Caixa_postal = db.Column(db.String(255))
    Status = db.Column(db.String(255))
    Pagamentos = db.Column(db.String(255))
    Enderecos = db.relationship('Clientesenderecos', backref='cliend')
    Contatos = db.relationship('Clientescontatos', backref='clicon')
    Contatosrealizados = db.relationship('Contatos_realizados', backref='crealizado')



class Clientesenderecos(db.Model):
    __tablename__ = 'clientesenderecos'
    Idclientesenderecos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Finalidade = db.Column('finalidade', db.String(255))
    Endereco = db.Column('endereco', db.String(255))
    Bairro = db.Column('bairro', db.String(255))
    Cidade = db.Column('cidade', db.String(255))
    Estado = db.Column('estado', db.String(255))
    Cep = db.Column('cep', db.String(255))
    idcliente = db.Column(db.Integer, db.ForeignKey('clientes.Idcliente'))


class Clientescontatos(db.Model):
    __tablename__ = "clientescontatos"
    Idclientecontato = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nome = db.Column(db.String(255))
    Cargo = db.Column(db.String(255))
    Telefone = db.Column(db.String(255))
    Ramal = db.Column(db.String(255))
    Celular = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    idcliente = db.Column(db.Integer, db.ForeignKey("clientes.Idcliente"))

class Contatos_realizados(db.Model):
    __tablename__ = "contatos_realizados"
    Id_contato_realizados = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Data_contato = db.Column(db.String(255))
    # Idcliente = db.Column(db.String(255))
    Pessoa_de_contato = db.Column(db.String(255))
    Metodo_de_contato = db.Column(db.String(255))
    Descricao = db.Column(db.String(255))
    idcliente = db.Column(db.Integer, db.ForeignKey("clientes.Idcliente"))


class Representadas(db.Model):
    __tablename__ = "representadas"
    Idrepresentada = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Razaosocial = db.Column(db.String(255))
    Cnpj = db.Column(db.String(255))
    Inscricaoestadual = db.Column(db.String(255))
    Telefone = db.Column(db.String(255))
    Endereco = db.Column(db.String(255))
    Bairro = db.Column(db.String(255))
    Cidade = db.Column(db.String(255))
    Estado = db.Column(db.String(255))
    Cep = db.Column(db.String(255))
    Comissao = db.Column(db.String(255))
    Contatos = db.relationship("Representadascontatos", backref="rcontato")


class Representadascontatos(db.Model):
    __tablename__ = "representadascontatos"
    Idcontatorepresentada = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nome = db.Column(db.String(255))
    Cargo = db.Column(db.String(255))
    Telefone = db.Column(db.String(255))
    Celular = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    #representada = db.relationship("Representadas", backref="repre")
    Idrepresentada = db.Column(db.Integer, db.ForeignKey("representadas.Idrepresentada"))


class Transportadoras(db.Model):
    __tablename__ = "transportadoras"
    idtransportadora = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Transportadora = db.Column("transportadora", db.String(255))
    Cidade = db.Column("cidade", db.String(255))
    Estado = db.Column("estado", db.String(255))
    Telefone = db.Column("telefone", db.String(255))


class ContasBancarias(db.Model):
    __tablename__ = "CONTASBANCARIAS"
    idcontasbancarias = db.Column(db.Integer, primary_key=True, autoincrement=True)
    banco = db.Column(db.Integer)
    agencia = db.Column(db.Integer)
    contabancaria = db.Column(db.Integer)
    codigoauxiliar = db.Column(db.String(255))


class NumerosOrcamentos(db.Model):
    __tablename__ = "numerosorcamentos"
    idnumeroorcamentos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idcliente = db.Column(db.Integer)
    cliente = db.Column(db.String(255))
    idrepresentada = db.Column(db.Integer)
    representada = db.Column(db.String(255))
    data = db.Column(db.DateTime)
    valor = db.Column(db.Float)


class Usuarios(db.Model):
    __tablename__ = "usuarios"
    idusuarios = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=True)


class Vendedores(db.Model):
    __tablename__ = "vendedores"
    idvendedor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    telefone = db.Column(db.String(255))
    celular = db.Column(db.String(255))
    email = db.Column(db.String(255))
    endereco = db.Column(db.String(255))
    bairro = db.Column(db.String(255))  
    cidade = db.Column(db.String(255)) 
    estado = db.Column(db.String(255))  
    cep = db.Column(db.String(255))  
    cpf = db.Column(db.String(255))  
    cnpj = db.Column(db.String(255))  
    areaatuacao = db.Column(db.String(255))
    comissao = db.Column(db.Integer)
    banco = db.Column(db.String(255))



class Visitas(db.Model):
    __tablename__ = "visita"
    idvisita = db.Column(db.Integer, primary_key=True)
    idcliente = db.Column(db.Integer)
    razaosocial = db.Column(db.String(255))
    idcontato = db.Column(db.Integer)
    contato = db.Column(db.String(255))  
    datadavisita = db.Column(db.DateTime)
    motivovisita = db.Column(db.String(255))



'''
class Pedidos(db.Model):
    idpedido = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idcliente = db.ForeignKey('Representadas', db.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    razaosocial = db.Column()
    idnumeroorcamento = db.IntegerField(blank=True, null=True)
    ordemdecompra = db.Column()
    idrepresentada = db.IntegerField(blank=True, null=True)
    representada = db.Column(db_column='Representada', )  
    datapedido = db.DateTimeField(db_column='DataPedido', blank=True, null=True)  
    dataprevista = db.DateTimeField(db_column='DataPrevista', blank=True, null=True)  
    descricao = db.TextField(blank=True, null=True)
    ipi = db.IntegerField(db_column='IPI', blank=True, null=True)  
    valor = db.IntegerField(db_column='Valor', blank=True, null=True)  
    idvendedor = db.IntegerField(blank=True, null=True)
    vendedor = db.Column(db_column='Vendedor', )  
    idtransportadora = db.IntegerField(blank=True, null=True)
    transportadora = db.Column(db_column='Transportadora', )  
'''
