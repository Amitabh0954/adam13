from marshmallow import Schema, fields, validates, ValidationError

class ProductUpdateSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    price = fields.Float()

    @validates('price')
    def validate_price(self, value):
        if isinstance(value, float) and value <= 0:
            raise ValidationError("Price must be a positive number")

#### 4. Implement a controller to expose the API for updating product details