# Epic Title: Product Catalog Management

class Product:
    def __init__(self, id: int, name: str, description: str, price: float, category_id: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id

    @staticmethod
    def validate_name(name: str) -> bool:
        return len(name) > 0

    @staticmethod
    def validate_description(description: str) -> bool:
        return len(description) > 0

    @staticmethod
    def validate_price(price: float) -> bool:
        return price > 0