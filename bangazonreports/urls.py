from django.urls import path
from .views import favorite_sellers_list, expensive_products_list, inexpensive_products_list

urlpatterns = [
    path('reports/favoritesellers', favorite_sellers_list),
    path('reports/expensiveproducts', expensive_products_list),
    path('reports/inexpensiveproducts', inexpensive_products_list)
]