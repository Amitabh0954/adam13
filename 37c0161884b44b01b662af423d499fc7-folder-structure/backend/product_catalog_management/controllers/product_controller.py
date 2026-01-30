# Epic Title: Add New Product

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product_catalog_management.services.product_service import ProductService
import json

product_service = ProductService()

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        product = product_service.add_new_product(name, price, description)
        if product:
            return JsonResponse({'message': 'Product added successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Invalid data or product already exists'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)