from flask import url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Deal(db.Model):
    _tablename = "deal"
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(128), nullable = False)
    imagePath = db.Column(db.String(500), nullable = True)
    title = db.Column(db.Text(), nullable = False)
    overview = db.Column(db.Text(), nullable = False)
    price = db.Column(db.String(20), nullable = False)
    shipping = db.Column(db.String(50), nullable = True)
    listPrice = db.Column(db.String(20), nullable = False)
    detail = db.Column(db.String(500), nullable = False)

class DealDetail(db.Model):
    _tablename = "deal_detail"
    id = db.Column(db.Integer, primary_key = True)
    detail_description = db.Column(db.Text(), nullable = False)
    expire = db.Column(db.String(200), nullable = True)
    main_poster = db.Column(db.String(500), nullable = False)
    link = db.Column(db.String(500), nullable = False)
    deal = db.Column(db.Integer, db.ForeignKey("deal.id"))