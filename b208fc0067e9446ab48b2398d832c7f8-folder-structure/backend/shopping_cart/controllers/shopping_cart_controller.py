# Epic Title: Save Shopping Cart for Logged-in Users

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


@csrf_exempt
def remove_from_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        user = request.user if request.user.is_authenticated else None
        session = Session.objects.get(pk=request.session.session_key)

        product = Product.objects.get(pk=product_id)
        shopping_cart_service.remove_product_from_cart(user, session, product)

        return JsonResponse({'message': 'Product removed from cart successfully'}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def modify_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        user = request.user if request.user.is_authenticated else None
        session = Session.objects.get(pk=request.session.session_key)

        product = Product.objects.get(pk=product_id)
        error_message = shopping_cart_service.modify_product_quantity(user, session, product, quantity)

        if error_message:
            return JsonResponse({'error': error_message}, status=400)
        return JsonResponse({'message': 'Product quantity updated successfully'}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def transfer_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            session = Session.objects.get(pk=request.session.session_key)
            shopping_cart_service.transfer_session_cart_to_user(request.user, session)
            return JsonResponse({'message': 'Shopping cart transferred successfully'}, status=200)
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)