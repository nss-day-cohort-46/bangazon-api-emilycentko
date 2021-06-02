from django.urls import path
from .views import favorite_sellers_list

urlpatterns = [
    path('reports/favoritesellers', favorite_sellers_list),
]