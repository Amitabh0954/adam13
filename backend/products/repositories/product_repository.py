# Epic Title: Add New Product

from backend.products.models.product import Product

class ProductRepository:
    def add_product(self, name: str, description: str, price: float) -> Product:
        if price <= 0:
            raise ValueError("Price must be a positive number")
        if not description:
            raise ValueError("Description cannot be empty")

        product = Product(name=name, description=description, price=price)
        product.save()
        return product

    def get_product_by_name(self, name: str) -> Product:
        return Product.objects.filter(name=name).first()

    def list_all_products(self) -> list[Product]:
        return Product.objects.all()