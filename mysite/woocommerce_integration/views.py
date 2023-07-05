from django.http import HttpResponse
from django.shortcuts import render
import requests


from woocommerce_integration.woocommerce import get_product_list

def my_view(request):
    products = get_product_list()

    if products is not None:
        
        product_str = '\n'.join([str(product) for product in products])
        return HttpResponse(f"Product List:\n{product_str}")
    else:
        return HttpResponse("Failed to fetch the product list.")

# print(wcapi.get("products").json())
