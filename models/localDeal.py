from deal import db


class LocalDeal(db.Model):
    __tablename__ = "local_deal"
    id = db.Column(db.Integer, primary_key = True)
    imagePath = db.Column(db.String(500), nullable = True)
    title = db.Column(db.Text(), nullable = False)
    overview = db.Column(db.Text(), nullable = False)
    source = db.Column(db.Text(), nullable = True)
    url = db.Column(db.Text(), nullable = False)
    sourceUrl = db.Column(db.Text(), nullable = True)
    city = db.Column(db.Text(), nullable = False)