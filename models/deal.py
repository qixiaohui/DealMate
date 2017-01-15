from flask import url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Deal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(128), nullable = False)
    imagePath = db.Column(db.String(500), nullable = True)
    title = db.Column(db.Text(), nullable = False)
    overview = db.Column(db.Text(), nullable = False)
    price = db.Column(db.String(20), nullable = False)
    shipping = db.Column(db.String(50), nullable = True)
    listPrice = db.Column(db.String(20), nullable = False)
    detail = db.Column(db.String(500), nullable = False)