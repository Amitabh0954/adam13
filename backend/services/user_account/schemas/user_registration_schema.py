from marshmallow import Schema, fields, validates, ValidationError
import re

class UserRegistrationSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str()
    last_name = fields.Str()

    @validates('password')
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        if not re.search(r"[A-Za-z]", value):
            raise ValidationError("Password must contain a letter")
        if not re.search(r"[0-9]", value):
            raise ValidationError("Password must contain a number")

#### 4. Implement a controller to expose the API for user registration

##### RegistrationController