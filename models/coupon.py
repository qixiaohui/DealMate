from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coupon(db.Model):
    __tablename__ = "coupon"
    id = db.Column(db.Integer, primary_key = True)
    link = db.Column(db.String(500), nullable = False)
    expire = db.Column(db.String(500), nullable = True)
    description = db.Column(db.Text(), nullable = False)