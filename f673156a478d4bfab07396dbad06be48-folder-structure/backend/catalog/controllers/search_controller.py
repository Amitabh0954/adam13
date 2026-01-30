# Epic Title: Search Products

from django.http import JsonResponse
from django.core.paginator import Paginator
from catalog.services.search_service import SearchService
import json

search_service = SearchService()

def search_products(request):
    query = request.GET.get('query', '')
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    products, total_count = search_service.search_products(query, int(page), int(page_size))
    response_data = {
        'total_count': total_count,
        'results': [product.to_dict() for product in products],
        'page': page,
        'page_size': page_size,
    }
    return JsonResponse(response_data, safe=False, status=200)