from django.shortcuts import render

def prod_list(request):
    return render(request, 'shop/prod_list.html')