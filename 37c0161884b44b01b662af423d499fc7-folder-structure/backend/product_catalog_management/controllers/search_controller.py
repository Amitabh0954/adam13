# Epic Title: Search Products

from django.http import JsonResponse
from product_catalog_management.services.search_service import SearchService
from django.views.decorators.csrf import csrf_exempt
import json

search_service = SearchService()

@csrf_exempt
def search_products(request):
    if request.method == 'GET':
        search_term = request.GET.get('search_term')
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 10))

        products = search_service.search_products(search_term, page, page_size)
        product_list = [{
            'id': product.id,
            'name': product.name,
            'price': str(product.price),
            'description': product.description,
            'created_at': product.created_at,
            'updated_at': product.updated_at
        } for product in products]

        return JsonResponse({'products': product_list}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)