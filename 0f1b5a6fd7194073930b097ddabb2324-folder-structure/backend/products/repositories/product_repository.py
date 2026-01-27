from backend.products.models.product import Product, product_category
from backend.auth.extensions import db

class ProductRepository:
    def get_product_by_name(self, name: str) -> Product:
        return Product.query.filter_by(name=name).first()

    def get_product_by_id(self, product_id: int) -> Product:
        return Product.query.filter_by(id=product_id).first()

    def create_product(self, name: str, price: float, description: str, category_ids: list[int]) -> Product:
        new_product = Product(name=name, price=price, description=description)
        for category_id in category_ids:
            category = Category.query.get(category_id)
            if category:
                new_product.categories.append(category)
        db.session.add(new_product)
        db.session.commit()
        return new_product

    def update_product(self, product: Product, category_ids: list[int] = None) -> Product:
        if category_ids is not None:
            product.categories.clear()
            for category_id in category_ids:
                category = Category.query.get(category_id)
                if category:
                    product.categories.append(category)
        db.session.commit()
        return product
    
    def delete_product(self, product_id: int):
        product = self.get_product_by_id(product_id)
        if product:
            product.is_active = False
            db.session.commit()

    def search_products(self, query: str, page: int, per_page: int):
        search = f"%{query}%"
        products = Product.query.filter(
            Product.is_active,
            db.or_(Product.name.like(search), Product.description.like(search)),
        ).paginate(page, per_page, False)
        return products.items, products.total