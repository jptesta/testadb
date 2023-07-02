# onde ficam as rotas

import os
from database import db
from flask import render_template, request, redirect, url_for, flash, Blueprint, current_app
from models.tables import Clientes, Clientescontatos, Clientesenderecos, Contatos_realizados, Representadas, \
    Representadascontatos

bp_default = Blueprint(
    "default",
    __name__,
    template_folder="../templates")

@bp_default.route('/')
def index():
    return render_template('index.html')

@bp_default.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        search = "%{0}%".format(search_value)
        results = Clientes.query.filter(Clientes.Razao_social.like(search)).all()
        return render_template('clientes.html', results=results)
    else:
        return redirect('clientes.html')

@bp_default.route("/cliente", methods=["GET", "POST"])
def cliente():
    my_data = db.session.query(Clientes).all()
    if request.method == "POST":
        razao_social = request.form['razao_social']
        nome_fantasia = request.form['nome_fantasia']
        cnpj = request.form['cnpj']
        inscricao_estadual = request.form['inscricao_estadual']
        telefone = request.form['telefone']
        celular = request.form['celular']
        email = request.form['email']
        danfe = request.form['danfe']
        site = request.form['site']
        vendedor = request.form['vendedor']
        visita = request.form['visita']
        observacoes = request.form['observacoes']
        caixa_postal = request.form['caixa_postal']
        status = request.form['status']
        pagamentos = request.form['pagamentos']
        my_data = Clientes(Razao_social=razao_social, Nome_fantasia=nome_fantasia, Cnpj=cnpj,
                           Inscricao_estadual=inscricao_estadual,
                           Telefone=telefone, Celular=celular,
                           Email=email, Danfe=danfe, Site=site,
                           Vendedor=vendedor, Visita=visita,
                           Observacoes=observacoes, Caixa_postal=caixa_postal, Status=status, Pagamentos=pagamentos)
        db.session.add(my_data)
        db.session.commit()
        # flash("Cliente cadastrado com sucessso!")
        return redirect(url_for('cliente'))
    return render_template("cliente.html", listaclientes=my_data)


# EDITAR CLIENTE
@bp_default.route('/editcliente/', methods=['GET', 'POST'])
def editcliente():
    if request.method == 'POST':
        my_data = Clientes.query.get(request.form.get('idcliente'))
        my_data.Idcliente = request.form['idcliente']
        my_data.Razao_social = request.form['razao_social']
        my_data.Nome_fantasia = request.form['nome_fantasia']
        my_data.Cnpj = request.form['cnpj']
        my_data.Inscricao_estadual = request.form['inscricao_estadual']
        my_data.Telefone = request.form['telefone']
        my_data.Celular = request.form['celular']
        my_data.Email = request.form['email']
        my_data.Danfe = request.form['danfe']
        my_data.Site = request.form['site']
        my_data.Vendedor = request.form['vendedor']
        my_data.Visita = request.form['visita']
        my_data.Observacoes = request.form['observacoes']
        my_data.Caixa_postal = request.form['caixa_postal']
        my_data.Status = request.form['status']
        my_data.Pagamentos = request.form['pagamentos']
        db.session.add(my_data)
        db.session.commit()
        # flash("Cliente alterado com sucesso!!")
        return redirect(url_for('cliente'))


# DELETAR CLIENTE
@bp_default.route('/deletecliente/<Idcliente>/', methods=['GET'])
def deletecliente(Idcliente):
    my_data = Clientes.query.get(Idcliente)
    db.session.delete(my_data)
    db.session.commit()
    # flash("Item deletado com sucesso!")
    return redirect(url_for('cliente'))


# CADASTRO DE ENDEREÇOS DE CLIENTES
@bp_default.route('/clientesenderecos', methods=['GET', 'POST'])
def clientesenderecos():
    my_data = db.session.query(Clientesenderecos).all()

    if request.method == "POST":
        finalidade = request.form['finalidade']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']
        my_data = Clientesenderecos(Finalidade=finalidade, Endereco=endereco, Bairro=bairro, Cidade=cidade,
                                    Estado=estado, Cep=cep)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('clientesenderecos'))

    return render_template('clientesenderecos.html', listaenderecos=my_data)


# EDIÇÃO DO ENDEREÇO DE CLIENTES
@bp_default.route('/editclientesenderecos', methods=['GET', 'POST'])
def editclientesenderecos():
    if request.method == "POST":
        my_data = Clientesenderecos.query.get(request.form.get("idclientesenderecos"))
        my_data.finalidade = request.form['finalidade']
        my_data.endereco = request.form['endereco']
        my_data.bairro = request.form['bairro']
        my_data.cidade = request.form['cidade']
        my_data.estado = request.form['estado']
        my_data.cep = request.form['cep']
        return redirect(url_for('clientesenderecos'))
    return render_template('clientesenderecos.html')


# CADASTROS DOS CONTATOS
@bp_default.route('/clientescontatos', methods=['GET', 'POST'])
def clientescontatos():
    my_data = db.session.query(Clientescontatos).all()
    if request.method == 'POST':
        nome = request.form['nome']
        cargo = request.form['cargo']
        telefone = request.form['telefone']
        ramal = request.form['ramal']
        celular = request.form['celular']
        email = request.form['email']
        my_data = Clientescontatos(Nome=nome, Cargo=cargo, Telefone=telefone, Ramal=ramal, Celular=celular, Email=email)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('clientescontatos'))
    return render_template('clientescontatos.html', listacontatos=my_data)


@bp_default.route('/editclientescontatos')
def editclientescontatos():
    my_data = Clientescontatos.query.get(request.form.get("idclientecontatos"))
    if request.method == 'POST':
        my_data.nome = request.form['nome']
        my_data.cargo = request.form['cargo']
        my_data.telefone = request.form['telefone']
        my_data.ramal = request.form['ramal']
        my_data.celular = request.form['celular']
        my_data.email = request.form['email']
        return redirect(url_for('clientescontatos'))
    return render_template('clientescontatos.html')


@bp_default.route('/deleteclientescontatos/<idclientecontato>')
def deleteclientescontatos(Idclientecontato):
    my_data = Clientescontatos.query.get(Idclientecontato)
    db.session.delete(my_data)
    db.session.commit()
    flash("contato deletado com sucesso")
    return redirect(url_for('clientescontatos'))



@bp_default.route('/solicitacoes')
def solicitacoes():
    return render_template('solicitacoes.html')

@bp_default.route('/orcamentos')
def orcamentos():
    return render_template('orcamentos.html')


@bp_default.route('/pedido')
def pedido():
    return render_template('pedido.html')


@bp_default.route('/contatosrealizados', methods=['GET', 'POST'])
def contatosrealizados():
    my_data = db.session.query(Contatos_realizados).all()
    if request.method == 'POST':
        data_contato = request.form['data_contato']
        cliente = request.form['cliente']
        pessoa_de_contato = request.form['pessoa_de_contato']
        metodo_de_contato = request.form['metodo_de_contato']
        descricao_contato = request.form['descricao_contato']
        my_data = Contatos_realizados(Data_contato=data_contato, Cliente=cliente, Pessoa_de_contato=pessoa_de_contato,
                                     Metodo_de_contato=metodo_de_contato, Descricao=descricao_contato)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('contatosrealizados'))
    return render_template('contatosrealizados.html', my_data=my_data)


# TESTES
@bp_default.route('/testes')
def testes():
    cli = db.session.query(Clientes).all()
    cliend = db.session.query(Clientesenderecos)
    clicon = db.session.query(Clientescontatos)
    return render_template("testes.html", listaclientes=cli, listaenderecos=cliend, listacontatos=clicon)


@bp_default.route('/pyscript')
def pyscript():
    return render_template('pyscript.html')


@bp_default.route('/javascript')
def javascript():
    return render_template('javascript.html')

@bp_default.route('/clientescompletos')
def clientescompletos():
    return render_template('clientescompletos.html')

@bp_default.route('/treeview')
def treeview():
    return render_template('treeview.html')
