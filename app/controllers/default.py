# onde ficam as rotas


from flask import render_template, request, redirect, url_for, flash


from app import app
from app import db
from app.models.tables import Clientes, Clientescontatos, Clientesenderecos, Contatos_realizados, Representadas, Representadascontatos, Transportadoras


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cliente", methods=["GET", "POST"])
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
        my_data = Clientes(Razao_social=razao_social,Nome_fantasia=nome_fantasia, Cnpj=cnpj, Inscricao_estadual=inscricao_estadual, 
                            Telefone=telefone, Celular=celular,
                           Email=email, Danfe=danfe, Site=site,
                            Vendedor=vendedor, Visita=visita, 
                            Observacoes=observacoes, Caixa_postal=caixa_postal, Status=status, Pagamentos=pagamentos)
        db.session.add(my_data)
        db.session.commit()
        #flash("Cliente cadastrado com sucessso!")
        return redirect(url_for('cliente'))
    return render_template("cliente.html",listaclientes = my_data)


#EDITAR CLIENTE
@app.route('/editcliente/', methods=['GET', 'POST'])
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
        #flash("Cliente alterado com sucesso!!")
        return redirect(url_for('cliente'))

#DELETAR CLIENTE
@app.route('/deletecliente/<Idcliente>/', methods=['GET'])
def deletecliente(Idcliente):
    my_data = Clientes.query.get(Idcliente)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Item deletado com sucesso!")
    return redirect(url_for('cliente'))

#CADASTRO DE ENDEREÇOS DE CLIENTES
@app.route('/clientesenderecos', methods=['GET', 'POST'])
def clientesenderecos():
    my_data = db.session.query(Clientesenderecos).all()
    
    if request.method == "POST":
        finalidade = request.form['finalidade']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        estado = request.form['estado']
        cep = request.form['cep']
        my_data = Clientesenderecos(Finalidade=finalidade,Endereco=endereco,Bairro=bairro,Cidade=cidade,Estado=estado,Cep=cep)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('clientesenderecos'))
    
    return render_template('clientesenderecos.html', listaenderecos=my_data)

#EDIÇÃO DO ENDEREÇO DE CLIENTES
@app.route('/editclientesenderecos', methods=['GET', 'POST'])
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

#CADASTROS DOS CONTATOS
@app.route('/clientescontatos', methods=['GET', 'POST'])
def clientescontatos():
    my_data = db.session.query(Clientescontatos).all()
    if request.method == 'POST':
        nome = request.form['nome']
        cargo = request.form['cargo']
        telefone = request.form['telefone']
        ramal = request.form['ramal']
        celular = request.form['celular']
        email = request.form['email']
        my_data = Clientescontatos(Nome=nome,Cargo=cargo,Telefone=telefone,Ramal=ramal,Celular=celular,Email=email)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('clientescontatos'))
    return render_template('clientescontatos.html', listacontatos = my_data)


@app.route('/editclientescontatos')
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

@app.route('/deleteclientescontatos/<idclientecontato>')
def deleteclientescontatos(Idclientecontato):
    my_data = Clientescontatos.query.get(Idclientecontato)
    db.session.delete(my_data)
    db.session.commit()
    flash("contato deletado com sucesso")
    return redirect(url_for('clientescontatos'))

#CADASTRO DE TRANSPORTADORA
@app.route('/transportadora', methods=['GET', 'POST'])
def transportadora():
    my_data = db.session.query(Transportadoras).all()
    if request.method == "POST":
        transportadora = request.form['transportadora']
        cidade = request.form['cidade']
        estado = request.form['estado']
        telefone = request.form['telefone']
        my_data = Transportadoras(Transportadora=transportadora, Cidade=cidade, Estado=estado, Telefone=telefone)
        db.session.add(my_data)
        db.session.commit()
        #flash("Dados inseridos com sucesso!")
        return redirect(url_for('transportadora'))

    return render_template('transportadora.html', listatransportadoras=my_data)


#ATUALIZAÇÃO DO CADASTRO DA TRANSPORTADORA
@app.route('/updatetransp/', methods=['POST', 'GET'])
def updatetransp():
    if request.method == "POST":
        my_data = Transportadoras.query.get(request.form.get('idtransportadora'))
        my_data.idtransportadora = request.form['idtransportadora']
        my_data.Transportadora = request.form['transportadora']
        my_data.Cidade = request.form['cidade']
        my_data.Estado = request.form['estado']
        my_data.Telefone = request.form['telefone']
        db.session.commit()
        #flash("Dados alterados com sucesso!")
        return redirect(url_for('transportadora', listatransportadoras=my_data))

#DELETAR A TRANSPORTADORA
@app.route('/deletetransp/<idtransportadora>/', methods=['GET'])
def deletetransp(idtransportadora):
    my_data = Transportadoras.query.get(idtransportadora)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Item deletado com sucesso!")
    return redirect(url_for('transportadora'))

#Cadastrar REPRESENTATADAS
@app.route('/representadas', methods=['GET', 'POST'])
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
        repres = Representadas(Razaosocial=razaosocial, Cnpj=cnpj, Inscricaoestadual=inscricaoestadual,Telefone=telefone,
                               Endereco=endereco,Bairro=bairro,Cidade=cidade,Estado=estado,Cep=cep, Comissao=comissao)
        db.session.add(repres)
        db.session.commit()
        #flash("Dados inseridos com sucesso!")
        return redirect(url_for('representadas'))
   
    return render_template('representadas.html', repre=repres)

@app.route('/editrepresentada/', methods=['GET', 'POST'])
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


@app.route('/deleterepres/<Idrepresentada>/', methods=['GET'])
def deleterepres(Idrepresentada):
    my_data = Representadas.query.get(Idrepresentada)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Item deletado com sucesso!")
    return render_template('representadas.html')

#cadastrar contatos das representadas
@app.route('/representadacontatos', methods=['GET', 'POST'])
def representadacontatos():
    reprecont = db.session.query(Representadascontatos).all()
    if request.method == 'POST':
        #flash('Cadastrado realizado')
        nome = request.form['nome']
        cargo = request.form['cargo']
        telefone = request.form['telefone']
        celular = request.form['celular']
        email = request.form['email']
        reprecont = Representadascontatos(Nome=nome,Cargo=cargo,Telefone=telefone,Celular=celular,Email=email)
        db.session.add(reprecont)
        db.session.commit()
        return redirect(url_for('representadacontatos'))
    return render_template('representadacontatos.html', listacontatosrepresentada=reprecont)

#editar contatos das representadas
@app.route('/editarrepresentadacontatos', methods=['GET', 'POST'])
def editarrepresentadacontatos():
    my_data = Representadascontatos.query.get(request.form.get("Idcontatorepresentada"))
    if request.method == 'POST':
        #flash('Cadastrado realizado')
        my_data.nome = request.form['nome']
        my_data.cargo = request.form['cargo']
        my_data.telefone = request.form['telefone']
        my_data.celular = request.form['celular']
        my_data.email = request.form['email']
        return redirect(url_for('representadacontatos', listacontatosrepresentada=my_data))
    return render_template('representadacontatos.html')


@app.route('/deleterepresentadacontatos/<Idcontatorepresentada>', methods=['GET'])
def deleterepresentadacontatos(Idcontatorepresentada):
    my_data = Representadascontatos.query.get(Idcontatorepresentada)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Item deletado com sucesso!")
    return render_template('representadacontatos.html')


@app.route('/contatosrealizados', methods=['GET', 'POST'])
def contatosrealizados():
    my_data = db.session.query(Contatos_realizados).all()
    return render_template('contatosrealizados.html', my_data=my_data)



#testes
@app.route('/testes')
def testes():
    cli = db.session.query(Clientes).all()
    cliend = db.session.query(Clientesenderecos)
    clicon = db.session.query(Clientescontatos)
    return render_template("testes.html", listaclientes=cli, listaenderecos=cliend, listacontatos=clicon)


@app.route('/pyscript')
def pyscript():
    return render_template('pyscript.html')


@app.route('/javascript')
def javascript():
    return render_template('javascript.html')
