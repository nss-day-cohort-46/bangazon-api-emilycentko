"""Module for generating products priced at $1000 or more"""

from django.shortcuts import render
from bangazonapi.models import Product
from bangazonreports.views import Connection


def expensive_products_list(request):

    expensive_products = Product.objects.filter(price__gte = 1000)

    template = 'products/list_of_expensive_products.html'
    context = {
            'expensive_products_list': expensive_products
        }

    return render(request, template, context)
    