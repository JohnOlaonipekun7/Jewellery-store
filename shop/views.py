from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def all_products(request):
    products = Product.objects.filter(available=True)
    
    paginator = Paginator(products, 6) 
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages) 
    return render(request, 'shop/prod_list.html', {'products': products})


def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, available=True)
    return render(request, 'shop/prod_list.html', {'category': category, 'products': products})


def product_detail(request, category_id, product_id):
    category = get_object_or_404(Category, id=category_id)
    product = get_object_or_404(Product, id=product_id, category=category)
    return render(request, 'shop/product.html', {'category': category, 'product': product})

