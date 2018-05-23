import datetime as dt

from marshmallow import Schema, fields

class Transaction():
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)

# We use the schema class to deserialize from JSON objects
# and to serialize to JSON objects
# Inherits from superclass Schema in marshmallow
class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()
