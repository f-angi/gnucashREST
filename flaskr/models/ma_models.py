from marshmallow import fields, Schema


class AccountSchema(Schema):
    name = fields.Str()
    type = fields.Str()


class SplitSchema(Schema):
    account = fields.Nested(AccountSchema)
    value = fields.Decimal()


class TransactionSchema(Schema):
    guid = fields.String()
    description = fields.String()
    date = fields.Date()
    amount = fields.Float()
    account_name = fields.String()
    account_type = fields.String()
