# onde ficam as rotas

from flask import render_template, request, redirect, url_for, flash 


from app import app
from app import db
from app.models.tables import Transportadoras



@app.route("/")
def index():
    return render_template("index.html")

#CADASTRO DE TRANSPORTADORA
@app.route('/transportadora', methods=['GET', 'POST'])
def transportadora():
    my_data = db.session.query(Transportadoras).all()
    if request.method == "POST":
        transportadora = request.form['transportadora']
        cidade = request.form['cidade']
        estado = request.form['estado']
        telefone = request.form['telefone']
        my_data = Transportadora(Transportadora=transportadora, Cidade=cidade, Estado=estado, Telefone=telefone)
        db.session.add(my_data)
        db.session.commit()
        #flash("Dados inseridos com sucesso!")
        return redirect(url_for('transportadora'))
    return render_template('transportadora.html', listatransportadoras=my_data)


#ATUALIZAÇÃO DO CADASTRO DA TRANSPORTADORA
@app.route('/updatetransp', methods=['POST', 'GET'])
def updatetransp():
    if request.method == "POST":
        my_data = Transportadoras.query.get(request.form.get('idtransportadora'))
        my_data.idtransportadora = request.form['idtransportadora']
        my_data.transportadora = request.form['transportadora']
        my_data.cidade = request.form['cidade']
        my_data.estado = request.form['estado']
        my_data.telefone = request.form['telefone']
        db.session.commit()
        #flash("Dados alterados com sucesso!")
        return redirect(url_for('transportadora'))

#DELETAR A TRANSPORTADORA

@app.route('/deletetransp/<string:idtransportadora>/', methods=['GET'])
def deletetransp(idtransportadora):
    my_data = Transportadoras.query.get(idtransportadora)
    db.session.delete(my_data)
    db.session.commit()
    #flash("Item deletado com sucesso!")
    return redirect(url_for('transportadora'))
