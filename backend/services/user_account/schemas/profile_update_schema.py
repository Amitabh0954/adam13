from marshmallow import Schema, fields, validates, ValidationError

class ProfileUpdateSchema(Schema):
    email = fields.Email()
    first_name = fields.Str()
    last_name = fields.Str()
    preferences = fields.Str()

#### 4. Implement a controller to expose the API for profile management