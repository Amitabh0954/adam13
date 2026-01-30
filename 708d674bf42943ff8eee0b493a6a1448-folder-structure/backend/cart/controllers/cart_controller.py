# Epic Title: Add Product to Shopping Cart

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from catalog.models.product import Product
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

        product = Product.objects.get(id=product_id)
        cart = cart_service.get_or_create_cart(user=request.user)

        if not product:
            return JsonResponse({'error': 'Product not found'}, status=404)

        cart_item = cart_service.add_product_to_cart(cart, product, quantity)
        return JsonResponse({'message': 'Product added to cart', 'cart_item_id': cart_item.id, 'quantity': cart_item.quantity}, status=201)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)