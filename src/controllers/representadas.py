from database import db
from flask import render_template, request, redirect, url_for, flash, Blueprint, current_app

from models.tables import Representadas, Representadascontatos

bp_representadas = Blueprint("representadas", __name__, template_folder="../templates")


# Cadastrar REPRESENTATADAS
@bp_representadas.route('/representadas', methods=['GET', 'POST'])
def representadas():
    repres = db.session.query(Representadas).all()
    if request.method == 'POST':
        razaosocial = request.form['razaosocial']
        cnpj = request.form['cnpj']
        inscricaoestadual = request.form['inscricaoestadual']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']
        comissao = request.form['comissao']
        repres = Representadas(Razaosocial=razaosocial, Cnpj=cnpj, Inscricaoestadual=inscricaoestadual,
                               Telefone=telefone,
                               Endereco=endereco, Bairro=bairro, Cidade=cidade, Estado=estado, Cep=cep,
                               Comissao=comissao)
        db.session.add(repres)
        db.session.commit()
        # flash("Dados inseridos com sucesso!")
        return redirect(url_for('representadas'))

    return render_template('representadas.html', repre=repres)


@bp_representadas.route('/editrepresentada/', methods=['GET', 'POST'])
def editrepresentada():
    my_data = Representadas.query.get(request.form.get("idrepresentadas"))
    if request.method == 'POST':
        my_data.razaosocial = request.form['razaosocial']
        my_data.cnpj = request.form['cnpj']
        my_data.inscricaoestadual = request.form['inscricaoestadual']
        my_data.telefone = request.form['telefone']
        my_data.endereco = request.form['endereco']
        my_data.bairro = request.form['bairro']
        my_data.cidade = request.form['cidade']
        my_data.estado = request.form['estado']
        my_data.cep = request.form['cep']
        my_data.comissao = request.form['comissao']
        return redirect(url_for('representadas', repres=my_data))
    return render_template('representadas.html')


@bp_representadas.route('/deleterepres/<Idrepresentada>/', methods=['GET'])
def deleterepres(Idrepresentada):
    my_data = Representadas.query.get(Idrepresentada)
    db.session.delete(my_data)
    db.session.commit()
    # flash("Item deletado com sucesso!")
    return render_template('representadas.html')

# cadastrar contatos das representadas
@bp_representadas.route('/representadacontatos', methods=['GET', 'POST'])
def representadacontatos():
    reprecont = db.session.query(Representadascontatos).all()
    if request.method == 'POST':
        # flash('Cadastrado realizado')
        nome = request.form['nome']
        cargo = request.form['cargo']
        telefone = request.form['telefone']
        celular = request.form['celular']
        email = request.form['email']
        reprecont = Representadascontatos(Nome=nome, Cargo=cargo, Telefone=telefone, Celular=celular, Email=email)
        db.session.add(reprecont)
        db.session.commit()
        return redirect(url_for('representadacontatos'))
    return render_template('representadacontatos.html', listacontatosrepresentada=reprecont)


# editar contatos das representadas
@bp_representadas.route('/editarrepresentadacontatos', methods=['GET', 'POST'])
def editarrepresentadacontatos():
    my_data = Representadascontatos.query.get(request.form.get("Idcontatorepresentada"))
    if request.method == 'POST':
        # flash('Cadastrado realizado')
        my_data.nome = request.form['nome']
        my_data.cargo = request.form['cargo']
        my_data.telefone = request.form['telefone']
        my_data.celular = request.form['celular']
        my_data.email = request.form['email']
        return redirect(url_for('representadacontatos', listacontatosrepresentada=my_data))
    return render_template('representadacontatos.html')


@bp_representadas.route('/deleterepresentadacontatos/<Idcontatorepresentada>', methods=['GET'])
def deleterepresentadacontatos(Idcontatorepresentada):
    my_data = Representadascontatos.query.get(Idcontatorepresentada)
    db.session.delete(my_data)
    db.session.commit()
    # flash("Item deletado com sucesso!")
    return render_template('representadacontatos.html')
