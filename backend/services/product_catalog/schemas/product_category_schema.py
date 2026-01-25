from marshmallow import Schema, fields, validates, ValidationError

class ProductCategorySchema(Schema):
    product_id = fields.Int(required=True)
    category_id = fields.Int(required=True)

#### 5. Implement a controller to expose the API for categorization