# Epic Title: Product Categorization

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product_catalog_management.services.category_service import CategoryService
import json

category_service = CategoryService()

@csrf_exempt
def add_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        parent_name = data.get('parent_name')

        category = category_service.add_category(name, parent_name)
        if category:
            return JsonResponse({'message': 'Category added successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Invalid data or parent category not found'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def get_categories(request):
    if request.method == 'GET':
        categories = category_service.get_all_categories()
        category_list = [{
            'id': category.id,
            'name': category.name,
            'parent_id': category.parent.id if category.parent else None
        } for category in categories]
        return JsonResponse({'categories': category_list}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def delete_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')

        if category_service.delete_category(name):
            return JsonResponse({'message': 'Category deleted successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Category not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)