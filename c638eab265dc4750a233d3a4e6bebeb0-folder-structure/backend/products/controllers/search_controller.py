# Epic Title: Search Products

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.services.search_service import SearchService
import json

search_service = SearchService()

@csrf_exempt
def search_products(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 10))

        search_results = search_service.search_products(query, page, page_size)
        return JsonResponse({'products': search_results}, status=200)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)