# Epic Title: Product Catalog Management

class Product:
    def __init__(self, id: int, name: str, description: str, price: float, category_id: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id