from flask_marshmallow import Marshmallow, fields
from deal import Deal, DealDetail

ma  = Marshmallow()


class DealSchema(ma.ModelSchema):
    class Meta:
        model = Deal

class DealDetailSchema(ma.ModelSchema):
    class Meta:
        model = DealDetail

deal_schema = DealSchema()
deals_schema = DealSchema(many = True)

deal_detail_schema = DealDetailSchema()
deals_detail_schema = DealDetailSchema(many = True)