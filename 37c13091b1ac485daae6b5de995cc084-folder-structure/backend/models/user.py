from backend.extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # Inline comment referencing the Epic Title
    # Epic Title: Product Catalog Management

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    preferences = db.Column(db.JSON, nullable=True)
    is_admin = db.Column(db.Boolean, default=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "preferences": self.preferences
        }