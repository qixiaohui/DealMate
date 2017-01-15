import sys
from flask import Flask, jsonify, abort, request
from models.deal import Deal, DealDetail, db
from scrape.categoryList import categoryList
from models.dealSchema import ma, deals_schema, deal_detail_schema
from scrape.dealScrapper import scrape_deal

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///review.db"
db.init_app(app)
ma.init_app(app)


@app.route("/deals/<category>/<subcategory>", methods = ["GET"])
def get_deals_by_category(category, subcategory = None):
    if subcategory is None:
        deals = Deal.query.filter_by(category = str(category)).all()
    else:
        deals = Deal.query.filter_by(category = str(category + "/" + subcategory)).all()
    return deals_schema.jsonify(deals)


@app.route("/detail/<int:id>", methods = ["GET"])
def get_deal_detail(id):
    if id is not None:
        deal_detail = DealDetail.query.filter_by(id = id).first()
    return deal_detail_schema.jsonify(deal_detail)


if __name__ == "__main__":
    if "create_db" in sys.argv:
        with app.app_context():
            db.create_all()
    elif "add_db" in sys.argv:
        db.app = app
        for item in categoryList().categoryList:
            if len(item) == 1:
                scrape_deal(db, item[0])
            elif len(item) == 2:
                scrape_deal(db, item[0], item[1])
    elif "check" in sys.argv:
        with app.app_context():
            deals = Deal.query.filter_by(category = "computers/laptops-ultrabooks").all()
            print(str(deals))
    else:
        app.run(debug=True, port=8000)




