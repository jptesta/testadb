from flask import render_template, request, redirect, url_for, flash, Blueprint, current_app
from database import db
from models.tables import Transportadoras

bp_transportadoras = Blueprint("transportadoras", __name__,template_folder="../templates")


# CADASTRO DE TRANSPORTADORA
@bp_transportadoras.route('/transportadora', methods=['GET', 'POST'])
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
        # flash("Dados inseridos com sucesso!")
        return redirect(url_for('transportadora'))

    return render_template('transportadora.html', listatransportadoras=my_data)


# ATUALIZAÇÃO DO CADASTRO DA TRANSPORTADORA
@bp_transportadoras.route('/updatetransp/', methods=['POST', 'GET'])
def updatetransp():
    if request.method == "POST":
        my_data = Transportadoras.query.get(request.form.get('idtransportadora'))
        my_data.idtransportadora = request.form['idtransportadora']
        my_data.Transportadora = request.form['transportadora']
        my_data.Cidade = request.form['cidade']
        my_data.Estado = request.form['estado']
        my_data.Telefone = request.form['telefone']
        db.session.commit()
        # flash("Dados alterados com sucesso!")
        return redirect(url_for('transportadora', listatransportadoras=my_data))


# DELETAR A TRANSPORTADORA
@bp_transportadoras.route('/deletetransp/<idtransportadora>/', methods=['GET'])
def deletetransp(idtransportadora):
    my_data = Transportadoras.query.get(idtransportadora)
    db.session.delete(my_data)
    db.session.commit()
    # flash("Item deletado com sucesso!")
    return redirect(url_for('transportadora'))


