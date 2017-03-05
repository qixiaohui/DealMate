from flask_marshmallow import Marshmallow, fields
from deal import Deal, DealDetail
from localDeal import LocalDeal

ma = Marshmallow()


class DealSchema(ma.ModelSchema):
    class Meta:
        model = Deal

class DealDetailSchema(ma.ModelSchema):
    class Meta:
        model = DealDetail

class LocalDealSchema(ma.ModelSchema):
    class Meta:
        model = LocalDeal

deal_schema = DealSchema()
deals_schema = DealSchema(many=True)

deal_detail_schema = DealDetailSchema()
deals_detail_schema = DealDetailSchema(many=True)

local_deal_schema = LocalDealSchema()
local_deals_schema = LocalDealSchema(many=True)