from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('category/<uuid:category_id>/', views.products_by_category, name='products_by_category'),
    path('category/<uuid:category_id>/product/<uuid:product_id>/', views.product_detail, name='product_detail'),
]
