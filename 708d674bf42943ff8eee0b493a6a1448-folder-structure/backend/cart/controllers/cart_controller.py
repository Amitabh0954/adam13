# Epic Title: Save Shopping Cart for Logged-in Users

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from catalog.models.product import Product
from cart.services.cart_service import CartService
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
import json

cart_service = CartService()

@csrf_exempt
@login_required
def add_product_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        if not product_id or quantity < 1:
            return JsonResponse({'error': 'Product ID and positive quantity are required'}, status=400)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

        cart = cart_service.get_or_create_cart(user=request.user)
        cart_item = cart_service.add_product_to_cart(cart, product, quantity)
        return JsonResponse({'message': 'Product added to cart', 'cart_item_id': cart_item.id, 'quantity': cart_item.quantity}, status=201)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
@login_required
def remove_product_from_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart_item_id = data.get('cart_item_id')
        confirmation = data.get('confirmation')

        if confirmation != 'yes':
            return JsonResponse({'error': 'Removal not confirmed'}, status=400)

        success = cart_service.remove_product_from_cart(cart_item_id)
        if success:
            return JsonResponse({'message': 'Product removed from cart'}, status=200)
        return JsonResponse({'error': 'Cart item not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
@login_required
def modify_quantity_in_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart_item_id = data.get('cart_item_id')
        quantity = data.get('quantity')

        if not cart_item_id or quantity < 1:
            return JsonResponse({'error': 'Valid cart_item_id and positive quantity are required'}, status=400)

        success = cart_service.modify_quantity_in_cart(cart_item_id, quantity)
        if success:
            return JsonResponse({'message': 'Quantity updated'}, status=200)
        return JsonResponse({'error': 'Cart item not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
@login_required
def save_cart_state(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        success = cart_service.save_cart_state(request.user)
        if success:
            return JsonResponse({'message': 'Cart state saved'}, status=200)
        return JsonResponse({'error': 'Unable to save cart state'}, status=500)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)