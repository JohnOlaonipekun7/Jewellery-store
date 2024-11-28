from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def all_products(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/prod_list.html', {'products': products})


def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, available=True)
    return render(request, 'shop/prod_list.html', {'category': category, 'products': products})


def product_detail(request, category_id, product_id):
    category = get_object_or_404(Category, id=category_id)
    product = get_object_or_404(Product, id=product_id, category=category)
    return render(request, 'shop/product.html', {'category': category, 'product': product})
