# Epic Title: Update Product Details

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.services.product_service import ProductService
import json

product_service = ProductService()

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        product = product_service.add_product(name, description, price)
        if product:
            return JsonResponse({'message': 'Product added successfully'}, status=201)
        return JsonResponse({'error': 'Product with this name already exists'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def list_products(request):
    if request.method == 'GET':
        products = product_service.get_all_products()
        product_list = [{'name': product.name, 'description': product.description, 'price': str(product.price)} for product in products]
        return JsonResponse({'products': product_list}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def update_product(request):
    if request.method == 'POST':
        if not request.user.is_staff:
            return JsonResponse({'error': 'Unauthorized access'}, status=403)
            
        data = json.loads(request.body)
        product_id = data.get('id')
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        product = product_service.update_product(product_id, name, description, price)
        if product:
            return JsonResponse({'message': 'Product updated successfully'}, status=200)
        return JsonResponse({'error': 'Product not found or invalid data'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)