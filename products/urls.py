from django.urls import path
from products.views import get_product, get_products

urlpatterns = [
    path('<slug>/' , get_product , name="get_product"),
    path('list', get_products, name ="get_products")
]