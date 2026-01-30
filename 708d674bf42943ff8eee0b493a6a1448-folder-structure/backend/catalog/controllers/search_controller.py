# Epic Title: Search Products

from django.http import JsonResponse
from catalog.services.search_service import SearchService
from django.core.paginator import Paginator
import json

search_service = SearchService()

def search_products(request):
    query = request.GET.get('query', '')
    page_number = request.GET.get('page', 1)
    page_size = 10

    products = search_service.search_products(query)
    paginator = Paginator(products, page_size)
    page = paginator.page(page_number)

    results = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "highlight": search_service.highlight_search_terms(product, query)
        }
        for product in page.object_list
    ]

    response = {
        "results": results,
        "total_pages": paginator.num_pages,
        "current_page": page.number
    }

    return JsonResponse(response)