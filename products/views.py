from django.shortcuts import render


def products(request):

    return render(request, 'products/products.html')


def product(request):

    return render(request, 'products/product.html')


def favorite(request):
    
    return render(request, 'products/favorite.html')


def shopping(request):

    return render(request, 'products/shopping-cart.html')