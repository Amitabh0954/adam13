# Epic Title: Product Categorization

from catalog.models.category import Category
from typing import Optional, List

class CategoryRepository:

    def create_category(self, name: str, parent_category: Optional[Category] = None) -> Category:
        category = Category(name=name, parent_category=parent_category)
        category.save()
        return category

    def get_category_by_name(self, name: str) -> Optional<Category]:
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    def get_all_categories(self) -> List[Category]:
        return list(Category.objects.all())