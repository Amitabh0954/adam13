# Epic Title: Delete Product

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


@csrf_exempt
def update_product(request, product_id: int):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        if price is not None and price <= 0:
            return JsonResponse({'error': 'Price must be a positive number'}, status=400)

        product = product_service.update_product(product_id, name, description, price)
        if product:
            return JsonResponse({'message': 'Product updated successfully'}, status=200)
        return JsonResponse({'error': 'Product not found or no changes made'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def delete_product(request, product_id: int):
    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')
        if confirmation != 'yes':
            return JsonResponse({'error': 'Deletion not confirmed'}, status=400)
        
        success = product_service.delete_product(product_id)
        if success:
            return JsonResponse({'message': 'Product deleted successfully'}, status=200)
        return JsonResponse({'error': 'Product not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)