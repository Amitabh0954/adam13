# Epic Title: Save Shopping Cart for Logged-in Users

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

@csrf_exempt
def remove_from_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        product_id = data.get('product_id')

        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)

        success = cart_service.remove_product_from_cart(user, product)
        if success:
            return JsonResponse({'message': 'Product removed from cart successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Product not found in cart'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def modify_product_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)

        cart_item = cart_service.modify_product_quantity(user, product, quantity)
        if cart_item:
            return JsonResponse({'message': 'Product quantity updated successfully', 'quantity': cart_item.quantity}, status=200)
        else:
            return JsonResponse({'message': 'Product removed from cart successfully'}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def get_cart(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        cart = cart_service.get_cart(user)
        if cart:
            items = [{
                'product_id': item.product.id,
                'product_name': item.product.name,
                'quantity': item.quantity
            } for item in cart.items.all()]
            return JsonResponse({'items': items}, status=200)
        else:
            return JsonResponse({'error': 'Cart not found'}, status=404)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)