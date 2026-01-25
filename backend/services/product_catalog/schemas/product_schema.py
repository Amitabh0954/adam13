from marshmallow import Schema, fields, validates, ValidationError

class ProductSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)

    @validates('price')
    def validate_price(self, value):
        if value <= 0:
            raise ValidationError("Price must be a positive number")

#### 4. Implement a controller to expose the API for adding new products