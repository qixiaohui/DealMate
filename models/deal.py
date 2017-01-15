from flask import url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Deal(db.Model):
    __tablename__ = "deal"
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(128), nullable = False)
    imagePath = db.Column(db.String(500), nullable = True)
    title = db.Column(db.Text(), nullable = False)
    overview = db.Column(db.Text(), nullable = False)
    price = db.Column(db.String(20), nullable = False)
    shipping = db.Column(db.String(50), nullable = True)
    listPrice = db.Column(db.String(20), nullable = False)
    detail = db.Column(db.String(500), nullable = False)
    detailId = db.Column(db.Integer, db.ForeignKey("deal_detail.id"))


class DealDetail(db.Model):
    __tablename__ = "deal_detail"
    id = db.Column(db.Integer, primary_key = True)
    detailDescription = db.Column(db.Text(), nullable = False)
    expire = db.Column(db.String(200), nullable = True)
    mainPoster = db.Column(db.String(500), nullable = False)
    link = db.Column(db.String(500), nullable = False)