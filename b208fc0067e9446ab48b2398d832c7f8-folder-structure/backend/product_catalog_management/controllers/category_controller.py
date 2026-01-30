# Epic Title: Product Categorization

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product_catalog_management.services.category_service import CategoryService
import json

category_service = CategoryService()

@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        parent_category_name = data.get('parent_category')

        category = category_service.create_category(name, parent_category_name)
        if category:
            return JsonResponse({'message': 'Category created successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Invalid category details or category already exists'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)