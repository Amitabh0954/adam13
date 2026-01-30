# Epic Title: Search Products

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
            return JsonResponse({'error': 'Invalid product details or product already exists'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def update_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        update_data = {key: value for key, value in data.items() if key != 'name'}

        product = product_service.update_product_details(name, **update_data)
        if product:
            return JsonResponse({'message': 'Product updated successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Product not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def delete_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')

        success = product_service.delete_product(name)
        if success:
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Product not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def search_products(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        page = int(request.GET.get('page', 1))
        items_per_page = int(request.GET.get('items_per_page', 10))

        products = product_service.search_products(query, page, items_per_page)
        product_list = [{
            'name': product.name,
            'price': str(product.price),
            'description': product.description
        } for product in products]

        return JsonResponse({'products': product_list}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)