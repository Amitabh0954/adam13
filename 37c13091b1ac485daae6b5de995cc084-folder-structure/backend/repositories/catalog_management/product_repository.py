from backend.models.product import Product
from backend.extensions import db

class ProductRepository:
    # Inline comment referencing the Epic Title
    # Epic Title: Product Catalog Management

    def find_by_name(self, name: str) -> Product:
        return Product.query.filter_by(name=name).first()
    
    def find_by_id(self, product_id: int) -> Product:
        return Product.query.get(product_id)
    
    def save_product(self, product: Product):
        db.session.add(product)
        db.session.commit()
    
    def update_product(self, product: Product):
        db.session.commit()

    def delete_product(self, product: Product):
        db.session.delete(product)
        db.session.commit()

    def search_products(self, query: str, page: int, per_page: int):
        search = f"%{query}%"
        results = Product.query.filter(
            Product.name.like(search) | Product.description.like(search)
        ).paginate(page, per_page, error_out=False)
        return results.items, results.total