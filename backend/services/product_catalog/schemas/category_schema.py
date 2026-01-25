from marshmallow import Schema, fields, validates, ValidationError

class CategorySchema(Schema):
    name = fields.Str(required=True)
    parent_id = fields.Int()

##### ProductCategory Schema