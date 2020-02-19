from marshmallow import fields, Schema


# class SplitSchema(Schema):
#     account = fields.Str()
#     value = fields.Decimal()


class TransactionSchema(Schema):
    post_date = fields.Date()
    description = fields.Str()
    amount = fields.Decimal()
    account = fields.Str()
    # splits = fields.List(fields.Nested(SplitSchema))
