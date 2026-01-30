# Epic Title: Add Product to Shopping Cart

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shopping_cart.services.shopping_cart_service import ShoppingCartService
from product_catalog_management.models.product import Product
from user_account_management.models.user import User
from django.contrib.sessions.models import Session
import json

shopping_cart_service = ShoppingCartService()

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        user = request.user if request.user.is_authenticated else None
        session = Session.objects.get(pk=request.session.session_key)

        product = Product.objects.get(pk=product_id)
        shopping_cart_service.add_product_to_cart(user, session, product, quantity)
        
        return JsonResponse({'message': 'Product added to cart successfully'}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def view_cart(request):
    if request.method == 'GET':
        user = request.user if request.user.is_authenticated else None
        session = Session.objects.get(pk=request.session.session_key)

        cart_items = shopping_cart_service.get_cart_items(user, session)
        items = [{'product_id': item.product.id, 'name': item.product.name, 'quantity': item.quantity} for item in cart_items]
        
        return JsonResponse({'cart_items': items}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)