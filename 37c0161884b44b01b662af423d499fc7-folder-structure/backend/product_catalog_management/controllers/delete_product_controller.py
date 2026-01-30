# Epic Title: Delete Product

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product_catalog_management.services.product_service import ProductService
import json

product_service = ProductService()

@csrf_exempt
def delete_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')

        if product_service.delete_product(product_id):
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Product not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)