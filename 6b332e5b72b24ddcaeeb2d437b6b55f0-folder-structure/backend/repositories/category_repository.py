# Epic Title: Product Categorization

from backend.models.category import Category
from typing import Optional, List

class CategoryRepository:

    def add_category(self, name: str, parent_id: Optional[int] = None) -> Category:
        parent = Category.objects.get(id=parent_id) if parent_id else None
        category = Category(
            name=name,
            parent=parent
        )
        category.save()
        return category

    def get_category_by_name(self, name: str) -> Optional[Category]:
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    def get_all_categories(self) -> List[Category]:
        return Category.objects.all()