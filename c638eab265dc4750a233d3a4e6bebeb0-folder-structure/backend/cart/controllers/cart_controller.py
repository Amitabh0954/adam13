# Epic Title: Save Shopping Cart for Logged-in Users

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cart.services.cart_service import CartService
from django.contrib.auth.decorators import login_required
import json

cart_service = CartService()

@csrf_exempt
@login_required
def add_product_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        cart_item = cart_service.add_product_to_cart(request.user, product_id, quantity)
        if cart_item:
            return JsonResponse({'message': 'Product added to cart successfully'}, status=201)
        return JsonResponse({'error': 'Failed to add product to cart'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
@login_required
def get_cart(request):
    if request.method == 'GET':
        cart_items = cart_service.get_cart_items(request.user)
        items = [{'product': item.product.name, 'quantity': item.quantity} for item in cart_items]
        return JsonResponse({'cart_items': items}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
@login_required
def remove_product_from_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')

        success = cart_service.remove_product_from_cart(request.user, product_id)
        if success:
            return JsonResponse({'message': 'Product removed from cart successfully'}, status=200)
        return JsonResponse({'error': 'Failed to remove product from cart or product not found in cart'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
@login_required
def modify_product_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        if quantity <= 0:
            return JsonResponse({'error': 'Quantity must be a positive integer'}, status=400)

        success = cart_service.modify_product_quantity(request.user, product_id, quantity)
        if success:
            return JsonResponse({'message': 'Product quantity updated successfully'}, status=200)
        return JsonResponse({'error': 'Failed to update product quantity or product not found in cart'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)