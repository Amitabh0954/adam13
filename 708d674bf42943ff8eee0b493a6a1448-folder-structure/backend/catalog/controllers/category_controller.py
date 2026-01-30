# Epic Title: Product Categorization

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from catalog.services.category_service import CategoryService
from catalog.models.category import Category
import json

category_service = CategoryService()

@csrf_exempt
def add_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        parent_category_name = data.get('parent_category')

        parent_category = None
        if parent_category_name:
            parent_category = category_service.get_category_by_name(parent_category_name)
            if not parent_category:
                return JsonResponse({'error': 'Parent category not found'}, status=404)

        category = category_service.add_category(name, parent_category)
        return JsonResponse({'message': 'Category added successfully', 'category_id': category.id}, status=201)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)