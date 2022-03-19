# onde ficam as rotas

from flask import render_template


from app import app 



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transportadora")
def transportadora():
    return render_template("transportadoras.html")

