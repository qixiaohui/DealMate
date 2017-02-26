import bs4 as bs
import urllib
import json
from models.coupon import Coupon

DEFAULT = object()


def scrape_coupon(db, category, subcategory = DEFAULT):
    base = "http://www.logicbuy.com/stores"
    src = urllib.urlopen(base)
    soup = bs.BeautifulSoup(src, 'html')
    coupons = soup.find("ul", {"id": "coupon_body"})
    couponList = coupons.findAll("li")
    for coupon in couponList:
        couponData = Coupon()
        try:
            description = coupon.find("h2", {"class": "coupon_title"}).text.strip()
            if description is not None:
                couponData.description = description
            expire = coupon.find("div", {"class": "exp_date"}).text.strip()
            if expire is not None:
                couponData.expire = expire
            link = 
        except AttributeError:


