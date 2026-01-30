# Epic Title: Update Product Details

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

    def update_product(self, name: str, new_description: str, new_price: float) -> Product:
        product = self.get_product_by_name(name)
        if not product:
            raise ValueError("Product not found")
        
        if new_price <= 0:
            raise ValueError("Price must be a positive number")
        
        if new_description.strip() == "":
            raise ValueError("Description cannot be empty")
        
        product.description = new_description
        product.price = new_price
        product.save()
        return product