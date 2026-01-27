from backend.repositories.catalog_management.product_repository import ProductRepository
from backend.models.product import Product
from backend.models.user import User
from backend.utils import pagination, highlight

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def add_product(self, data: dict) -> dict:
        name = data.get("name")
        price = data.get("price")
        description = data.get("description")
        category_ids = data.get("category_ids")

        if not name or self.product_repository.find_by_name(name):
            raise ValueError("Product name must be unique.")
        
        if not price or price <= 0:
            raise ValueError("Product price must be a positive number.")
        
        if not description:
            raise ValueError("Product description cannot be empty.")
        
        if not category_ids or len(category_ids) == 0:
            raise ValueError("Product must belong to at least one category.")

        new_product = Product(name=name, price=price, description=description)
        new_product.categories = category_ids
        self.product_repository.save_product(new_product)
        return new_product.to_dict()

    def update_product(self, user: User, product_id: int, data: dict) -> dict:
        if not user.is_admin:
            raise ValueError("Only admins can update the product details.")
        
        product = self.product_repository.find_by_id(product_id)
        
        if not product:
            raise ValueError("Product not found.")
        
        if 'price' in data:
            price = data['price']
            if not isinstance(price, (int, float)) or price <= 0:
                raise ValueError("Product price must be a positive number.")
            product.price = price
        
        if 'description' in data:
            description = data['description']
            if description:
                product.description = description
            else:
                raise ValueError("Product description cannot be empty.")
        
        if 'category_ids' in data:
            category_ids = data['category_ids']
            if not category_ids or len(category_ids) == 0:
                raise ValueError("Product must belong to at least one category.")
            product.categories = category_ids
        
        self.product_repository.update_product(product)
        return product.to_dict()

    def delete_product(self, user: User, product_id: int):
        if not user.is_admin:
            raise ValueError("Only admins can delete products.")
        
        product = self.product_repository.find_by_id(product_id)
        
        if not product:
            raise ValueError("Product not found.")
        
        self.product_repository.delete_product(product)

    def search_products(self, term: str, page: int, per_page: int):
        query = self.product_repository.search(term)
        paginated_results = pagination(query, page, per_page)
        
        results = []
        for product in paginated_results.items:
            product_dict = product.to_dict()
            product_dict['name'] = highlight(product_dict['name'], [term])
            product_dict['description'] = highlight(product_dict['description'], [term])
            results.append(product_dict)
        
        return {
            "products": results,
            "page": paginated_results.page,
            "pages": paginated_results.pages,
            "total": paginated_results.total
        }