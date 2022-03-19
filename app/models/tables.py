#declaraçao das tabelas
from app import db

class User(db.Model):
    __tablename__ = "Users"
    id = id.Column(db.Integer, primary_key=True)
    

