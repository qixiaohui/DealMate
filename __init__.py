import sys
from flask import Flask, jsonify, abort, request
from models.deal import Deal, DealDetail, db
from models.localDeal import LocalDeal
from scrape.categoryList import categoryList
from models.dealSchema import ma, deals_schema, deal_detail_schema, local_deals_schema
from scrape.dealScrapper import scrape_deal
from scrape.localDealScraper import scrape_deal as scrape_local_deal

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///review.db"
db.init_app(app)
ma.init_app(app)

# create new table for db initializaiton
with app.app_context():
    db.create_all()


@app.route("/deals/<category>", methods = ["GET"])
@app.route("/deals/<category>/<subcategory>", methods = ["GET"])
def get_deals_by_category(category, subcategory=None):
    if subcategory is None:
        deals = Deal.query.filter_by(category=str(category)).all()
    else:
        deals = Deal.query.filter_by(category=str(category + "/" + subcategory)).all()
    return deals_schema.jsonify(deals)


@app.route("/detail/<int:id>", methods = ["GET"])
def get_deal_detail(id):
    if id is not None:
        deal_detail = DealDetail.query.filter_by(id = id).first()
    return deal_detail_schema.jsonify(deal_detail)


@app.route("/search", methods = ["GET"])
def query_deals():
    query = request.args.get('content')
    search_result = []
    search_result.extend(Deal.query.filter(Deal.category.contains(query)).all());
    search_result.extend(Deal.query.filter(Deal.title.contains(query)).all());
    search_result.extend(Deal.query.filter(Deal.overview.contains(query)).all());
    if search_result is None:
        return []
    else:
        return deals_schema.jsonify(search_result)


@app.route("/local/<city>", methods = ["GET"])
def local_deal(city):
    res = LocalDeal.query.filter_by(city=city).all()
    if res is None or len(res) == 0:
        scrape_local_deal(db, city)
        res = LocalDeal.query.filter_by(city=city).all()
        return local_deals_schema.jsonify(res)
    return local_deals_schema.jsonify(res)


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
            deals = Deal.query.filter_by(category="computers/laptops-ultrabooks").all()
            print(str(deals))
    else:
        app.run()




