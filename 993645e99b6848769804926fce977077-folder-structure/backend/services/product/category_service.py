from backend.repositories.product.category_repository import CategoryRepository
from backend.models.category import Category

class CategoryService:
    
    def __init__(self):
        self.category_repository = CategoryRepository()

    def add_category(self, name: str, parent_id: int = None) -> None:
        if self.category_repository.get_category_by_name(name):
            raise ValueError("Category name already exists")

        if parent_id:
            parent_category = self.category_repository.get_category_by_id(parent_id)
            if not parent_category:
                raise ValueError("Parent category not found")
            new_category = Category(name=name, parent_id=parent_id)
        else:
            new_category = Category(name=name)

        self.category_repository.save_category(new_category)
    
    def delete_category(self, category_id: int) -> None:
        category = self.category_repository.get_category_by_id(category_id)
        if not category:
            raise ValueError("Category not found")

        self.category_repository.delete_category(category)