# Epic Title: Update Product Details

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product_catalog_management.services.product_service import ProductService
import json

product_service = ProductService()

@csrf_exempt
def update_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')

        product = product_service.update_product(product_id, name, price, description)
        if product:
            return JsonResponse({'message': 'Product updated successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid data or product not found'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)