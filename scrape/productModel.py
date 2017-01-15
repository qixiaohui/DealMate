import json


class product:
    def __init__(self, category = None, imagePath = None, title = None, overview = None, price = None, shipping = None, listPrice = None, detail = None):
        self.category = category
        self.imagePath = imagePath
        self.title = title
        self.overview = overview
        self.price = price
        self.shipping = shipping
        self.listPrice = listPrice
        self.detail = detail

    @property
    def category(self):
        return self.category

    @category.setter
    def category(self, value):
        self.category = str(value.decode("utf-8"))

    @property
    def imagePath(self):
        return self.imagePath

    @imagePath.setter
    def imagePath(self, value):
        self.imagePath = str(value.decode("utf-8"))

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        self.title = str(value.decode("utf-8"))

    @property
    def overview(self):
        return self.overview

    @overview.setter
    def overview(self, value):
        self.overview = str(value.decode("utf-8"))

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        self.price = str(value.decode("utf-8"))

    @property
    def shipping(self):
        return self.shipping

    @shipping.setter
    def shipping(self, value):
        self.shipping = str(value.decode("utf-8"))

    @property
    def listPrice(self):
        return self.listPrice

    @category.setter
    def listPrice(self, value):
        self.listPrice = str(value.decode("utf-8"))

    def obj_dict(obj):
        return obj.__dict__
