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

        if not name or not description or price is None:
            return JsonResponse({'error': 'All fields are required'}, status=400)
        
        if price <= 0:
            return JsonResponse({'error': 'Price must be a positive number'}, status=400)

        product = product_service.add_product(name, description, price)
        if product:
            return JsonResponse({'message': 'Product added successfully'}, status=201)
        return JsonResponse({'error': 'Product with this name already exists'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)