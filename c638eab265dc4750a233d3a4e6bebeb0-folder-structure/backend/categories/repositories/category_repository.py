# Epic Title: Product Categorization

from categories.models.category import Category
from typing import Optional, List

class CategoryRepository:

    def add_category(self, name: str, parent: Optional[Category]) -> Category:
        category = Category(name=name, parent=parent)
        category.save()
        return category

    def get_category_by_name(self, name: str) -> Optional<Category]:
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    def get_category_by_id(self, category_id: int) -> Optional<Category]:
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None

    def get_all_categories(self) -> List<Category]:
        return list(Category.objects.all())

    def delete_category_by_id(self, category_id: int) -> bool:
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return True
        except Category.DoesNotExist:
            return False