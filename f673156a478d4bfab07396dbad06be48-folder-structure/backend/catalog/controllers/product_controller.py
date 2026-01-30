# Epic Title: Add New Product

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from catalog.services.product_service import ProductService
import json

product_service = ProductService()

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        category_id = data.get('category_id')

        if not name or not description:
            return JsonResponse({'error': 'Name and description are required'}, status=400)
        
        if price is None or price <= 0:
            return JsonResponse({'error': 'Price must be a positive number'}, status=400)
        
        success, message = product_service.add_product(name, description, price, category_id)
        
        if success:
            return JsonResponse({'message': 'Product added successfully'}, status=201)
        else:
            return JsonResponse({'error': message}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)