# Epic Title: Product Categorization

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from categories.services.category_service import CategoryService
import json

category_service = CategoryService()

@csrf_exempt
def add_category(request):
    if request.method == 'POST':
        if not request.user.is_staff:
            return JsonResponse({'error': 'Unauthorized access'}, status=403)

        data = json.loads(request.body)
        name = data.get('name')
        parent_id = data.get('parent_id')

        category = category_service.add_category(name, parent_id)
        if category:
            return JsonResponse({'message': 'Category added successfully'}, status=201)
        return JsonResponse({'error': 'Category with this name already exists or invalid parent category'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def list_categories(request):
    if request.method == 'GET':
        categories = category_service.get_all_categories()
        category_list = [{'id': category.id, 'name': category.name, 'parent_id': category.parent.id if category.parent else None} for category in categories]
        return JsonResponse({'categories': category_list}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def delete_category(request):
    if request.method == 'POST':
        if not request.user.is_staff:
            return JsonResponse({'error': 'Unauthorized access'}, status=403)

        data = json.loads(request.body)
        category_id = data.get('id')

        success = category_service.delete_category(category_id)
        if success:
            return JsonResponse({'message': 'Category deleted successfully'}, status=200)
        return JsonResponse({'error': 'Category not found or already deleted'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)