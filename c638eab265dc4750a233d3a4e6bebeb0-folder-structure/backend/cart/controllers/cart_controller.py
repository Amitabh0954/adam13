# Epic Title: Add Product to Shopping Cart

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