# Epic Title: Add Product to Shopping Cart

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shopping_cart_management.services.cart_service import CartService
from product_catalog_management.models.product import Product
from user_account_management.models.user import User
import json

cart_service = CartService()

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)

        cart_item = cart_service.add_product_to_cart(user, product, quantity)
        if cart_item:
            return JsonResponse({'message': 'Product added to cart successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Unable to add product to cart'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)