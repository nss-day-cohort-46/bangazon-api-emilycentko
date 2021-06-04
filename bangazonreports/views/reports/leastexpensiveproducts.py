"""Module for generating products priced at $1000 or more"""
from django.shortcuts import render
from bangazonapi.models import Product
from bangazonreports.views import Connection


def inexpensive_products_list(request):

    least_expensive_products = Product.objects.filter(price__lte = 999)

    template = 'products/list_of_inexpensive_products.html'
    context = {
            'inexpensive_products_list': least_expensive_products
        }

    return render(request, template, context)