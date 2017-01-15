from flask_marshmallow import Marshmallow, fields
from deal import Deal

ma  = Marshmallow()


class DealSchema(ma.ModelSchema):
    class Meta:
        model = Deal

deal_schema = DealSchema()
deals_schema = DealSchema(many = True)