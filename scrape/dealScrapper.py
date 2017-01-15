import bs4 as bs
import urllib
import json
from models.deal import Deal, DealDetail


DEFAULT = object()


def scrape_deal(db, category, subcategory = DEFAULT):
    base = "http://www.logicbuy.com/categorydeals/"
    if subcategory is DEFAULT:
        base = base + category
        categoryHolder = category
    else:
        base = base + category + "/"+ subcategory
        categoryHolder = category + "/" + subcategory
    print(categoryHolder)
    src = urllib.urlopen(base)
    soup = bs.BeautifulSoup(src, 'html')
    deals = soup.find("div", {"class": "newest-deals"})
    # find the parent list view
    ulList = deals.find("ul", {"class": "deal-list"})
    productList = ulList.findAll("li")
    for index, product in enumerate(productList):
        product_data = Deal()
        product_detail_data = DealDetail()
        try:
            product_data.category = categoryHolder
            if product is None:
                continue
            imgs = product.findAll("img", src = True)
            # set image url
            if len(imgs) >= 2:
                product_data.imagePath = imgs[1]["src"]
            dealDeck = product.find("div", {"class": "deal-deck"})
            title = dealDeck.find("h2").find("a").text.strip()
            # set product title
            if title is not None:
                product_data.title = title
            urlPath = dealDeck.find("h2").find("a", href = True)["href"]
            # set product url
            if urlPath is not None:
                product_data.detail = urlPath
            desc = dealDeck.find("p", recursive = False).text.strip()
            # set product description
            if desc is not None:
                product_data.overview = desc
            dealPrice = product.find("div", {"class": "org-price"}).find("span").text.strip()
            shipping = product.find("div", {"class": "org-price"}).find("strong").find("span").text.strip()
            # set deal price
            if dealPrice is not None:
                product_data.price = dealPrice
            # set shipping
            if shipping is not None:
                product_data.shipping = shipping
            originalPrice = product.find("div", {"class": "list-save"}).find("strike").text.strip()
            if originalPrice is not None:
                product_data.listPrice = originalPrice
            #product_data = json.dumps(product_data.__dict__)
            detail_url = "http://www.logicbuy.com" + product_data.detail
            src = urllib.urlopen(detail_url)
            soup = bs.BeautifulSoup(src, "html")
            img_container = soup.find("div", {"class": "img-container"})
            img_url = img_container.find("img", {"class": "deals_image"}, src = True)["src"]
            if img_url is not None:
                product_detail_data.mainPoster = img_url
            product_desc = soup.find("div", {"class": "prod-desc"}).encode('utf-8').strip()
            if product_desc is not None:
                product_detail_data.detailDescription = json.dumps(product_desc)
            expire_div = soup.find("div", {"class": "expire-date"})
            expire = expire_div.find("span").text.strip()
            if expire is not None:
                product_detail_data.expire = expire
            get_deal = soup.find("a", {"class": "get-deal"}, href = True)["href"]
            if get_deal is not None:
                product_detail_data.link = get_deal
            db.session.add(product_detail_data)
            db.session.add(product_data)
            db.session.commit()
            print(index)
        except AttributeError:
            break










        


