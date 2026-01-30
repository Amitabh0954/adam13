# Epic Title: Product Categorization

from typing import Optional, List
from product_catalog_management.models.category import Category

class CategoryRepository:

    def create_category(self, name: str, parent: Optional[Category] = None) -> Category:
        category = Category(name=name, parent=parent)
        category.save()
        return category

    def get_category_by_name(self, name: str) -> Optional<Category]:
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    def get_all_categories(self) -> List[Category]:
        return list(Category.objects.all())

    def delete_category(self, category: Category) -> None:
        category.delete()