from backend.repositories.catalog_management.category_repository import CategoryRepository
from backend.models.category import Category

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, data: dict) -> dict:
        name = data.get("name")
        parent_id = data.get("parent_id")

        if not name or self.category_repository.find_by_name(name):
            raise ValueError("Category name must be unique.")
        
        new_category = Category(name=name, parent_id=parent_id)
        self.category_repository.save_category(new_category)
        return new_category.to_dict()

    def update_category(self, category_id: int, data: dict) -> dict:
        category = self.category_repository.find_by_id(category_id)
        
        if not category:
            raise ValueError("Category not found.")
        
        if 'name' in data:
            name = data['name']
            if name:
                existing_category = self.category_repository.find_by_name(name)
                if existing_category and existing_category.id != category_id:
                    raise ValueError("Category name must be unique.")
                category.name = name

        if 'parent_id' in data:
            parent_id = data['parent_id']
            category.parent_id = parent_id
        
        self.category_repository.update_category(category)
        return category.to_dict()

    def delete_category(self, category_id: int):
        category = self.category_repository.find_by_id(category_id)
        
        if not category:
            raise ValueError("Category not found.")
        
        self.category_repository.delete_category(category)