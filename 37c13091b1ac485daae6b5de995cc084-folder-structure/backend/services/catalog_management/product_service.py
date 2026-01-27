from backend.repositories.catalog_management.product_repository import ProductRepository
from backend.models.product import Product

class ProductService:
    # Inline comment referencing the Epic Title
    # Epic Title: Product Catalog Management

    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, data: dict) -> dict:
        name = data.get("name")
        price = data.get("price")
        description = data.get("description")

        if not name or self.product_repository.find_by_name(name):
            raise ValueError("Product name must be unique.")
        
        if not price or price <= 0:
            raise ValueError("Product price must be a positive number.")
        
        if not description:
            raise ValueError("Product description cannot be empty.")

        new_product = Product(name=name, price=price, description=description)
        self.product_repository.save_product(new_product)
        return new_product.to_dict()

    def update_product(self, product_id: int, data: dict) -> dict:
        product = self.product_repository.find_by_id(product_id)
        if not product:
            raise ValueError("Product not found")

        name = data.get("name")
        price = data.get("price")
        description = data.get("description")

        if name and name != product.name:
            if self.product_repository.find_by_name(name):
                raise ValueError("Product name must be unique.")
            product.name = name
        
        if price is not None:
            if price <= 0:
                raise ValueError("Product price must be a positive number.")
            product.price = price
        
        if description:
            product.description = description

        self.product_repository.update_product(product)
        return product.to_dict()

    def delete_product(self, product_id: int):
        product = self.product_repository.find_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        
        self.product_repository.delete_product(product)

    def search_products(self, query: str, page: int, per_page: int) -> tuple:
        results, total = self.product_repository.search_products(query, page, per_page)
        highlighted_results = []
        for product in results:
            product_dict = product.to_dict()
            product_dict["name"] = self.highlight_query(product_dict["name"], query)
            product_dict["description"] = self.highlight_query(product_dict["description"], query)
            highlighted_results.append(product_dict)
        return highlighted_results, total

    def highlight_query(self, text: str, query: str) -> str:
        highlighted = text.replace(query, f"<mark>{query}</mark>")
        return highlighted