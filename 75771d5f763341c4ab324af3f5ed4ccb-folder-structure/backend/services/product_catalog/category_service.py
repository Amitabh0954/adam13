# Epic Title: Product Categorization

from repositories.product_catalog.category_repository import CategoryRepository

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, data: dict) -> dict:
        category_data = {
            'name': data['name'],
            'parent_id': data.get('parent_id')
        }
        category_id = self.category_repository.save_category(category_data)
        return {"msg": "Category added successfully", "category_id": category_id}

    def update_category(self, category_id: int, data: dict) -> dict:
        updated_data = {
            'name': data['name'],
            'parent_id': data.get('parent_id')
        }
        self.category_repository.update_category(category_id, updated_data)
        return {"msg": "Category updated successfully"}