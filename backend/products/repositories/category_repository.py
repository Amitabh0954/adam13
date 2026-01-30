# Epic Title: Product Categorization

from backend.products.models.category import Category
from typing import List

class CategoryRepository:
    def add_category(self, name: str, parent: Category = None) -> Category:
        category = Category(name=name, parent=parent)
        category.save()
        return category

    def get_category_by_name(self, name: str) -> Category:
        return Category.objects.filter(name=name).first()

    def list_all_categories(self) -> List[Category]:
        return Category.objects.all()

    def delete_category(self, name: str) -> None:
        category = self.get_category_by_name(name)
        if not category:
            raise ValueError("Category not found")

        category.delete()