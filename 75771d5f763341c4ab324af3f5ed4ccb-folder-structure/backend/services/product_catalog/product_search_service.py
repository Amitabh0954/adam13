# Epic Title: Search Products

from repositories.product_catalog.product_repository import ProductRepository

class ProductSearchService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def search_products(self, params: dict) -> dict:
        query = params.get('query', '')
        page = int(params.get('page', 1))
        limit = int(params.get('limit', 10))
        offset = (page - 1) * limit

        products = self.product_repository.search_products(query, limit, offset)
        highlighted_results = self.highlight_search_terms(products, query)
        return {
            'products': highlighted_results,
            'page': page,
            'limit': limit,
            'total': self.product_repository.count_products(query)
        }

    def highlight_search_terms(self, products: list, query: str) -> list:
        highlighted_results = []
        for product in products:
            product['name'] = product['name'].replace(query, f"<mark>{query}</mark>")
            product['description'] = product['description'].replace(query, f"<mark>{query}</mark>")
            highlighted_results.append(product)
        return highlighted_results