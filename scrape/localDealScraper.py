import bs4 as bs
import urllib
from models.localDeal import LocalDeal
import sqlite3


DEFAULT = object()


def scrape_deal(db, city):
    url = "https://www.8coupons.com/city/" + city
    src = urllib.urlopen(url)
    dom = bs.BeautifulSoup(src, "html")
    deals = dom.find_all("div", {"class": "deal"})
    for index, deal in enumerate(deals):
        try:
            local_deal = LocalDeal()
            local_deal.imagePath = __convert__(deal.find("a").find("img", src=True)["src"])
            desc = deal.find("div", {"class": "description"})
            if desc is None:
                pass
            local_deal.title \
                = __convert__(desc.find("div", {"class": "dealSaving"}).find("a").text.strip())
            local_deal.overview \
                = __convert__(desc.find("div", {"class": "pull-left"}).find("small").text.strip())
            local_deal.source \
                = __convert__(desc.find("div", {"class": "pull-right"}).find("small").text.strip())
            local_deal.url \
                = __convert__(desc.find("div", {"class": "pull-right"}).find("a", href=True)["href"])
            local_deal.sourceUrl \
                = __convert__(desc.find("div", {"class": "pull-left"}).find("a", href=True)["href"])
            local_deal.city = __convert__(city)
            db.session.add(local_deal)
            db.session.commit()
            print(index)
        except (AttributeError, TypeError, sqlite3.ProgrammingError) as e:
            print(e)
            pass


def __convert__(source):
    try:
        unicode(source, "utf-8")
    except TypeError:
        return source

