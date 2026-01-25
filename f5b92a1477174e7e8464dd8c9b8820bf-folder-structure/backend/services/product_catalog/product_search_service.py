from backend.repositories.product.product_repository import ProductRepository

class ProductSearchService:
    
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, query: str, page: int, per_page: int):
        products, total = self.product_repository.search_products(query, page, per_page)
        highlighted_results = self.highlight_query_in_results(products, query)
        return highlighted_results, total

    def highlight_query_in_results(self, products, query):
        highlighted_products = []
        for product in products:
            highlighted_name = product.name.replace(query, f"<strong>{query}</strong>")
            highlighted_description = product.description.replace(query, f"<strong>{query}</strong>")
            highlighted_products.append({
                "id": product.id,
                "name": highlighted_name,
                "price": product.price,
                "description": highlighted_description,
                "category_id": product.category_id,
                "category": product.category.name if product.category else None
            })
        return highlighted_products