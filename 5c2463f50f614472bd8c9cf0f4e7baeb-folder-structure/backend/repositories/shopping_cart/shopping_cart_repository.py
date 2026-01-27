from backend.models.shopping_cart import ShoppingCartItem
from backend.extensions import db

class ShoppingCartRepository:
    def find_by_user_id(self, user_id: int) -> list[ShoppingCartItem]:
        return ShoppingCartItem.query.filter_by(user_id=user_id).all()

    def find_by_user_id_and_product_id(self, user_id: int, product_id: int) -> ShoppingCartItem:
        return ShoppingCartItem.query.filter_by(user_id=user_id, product_id=product_id).first()

    def save_item(self, item: ShoppingCartItem):
        db.session.add(item)
        db.session.commit()

    def delete_item(self, item: ShoppingCartItem):
        db.session.delete(item)
        db.session.commit()

    def update_item(self, item: ShoppingCartItem):
        db.session.commit()