from django.shortcuts import render
from .models import Product
def product_list(request):
    if not Product.objects.exists():
        Product.objects.create(name='Laptop',description='High performance laptop',price='1200')
        Product.objects.create(name='Mobile',description='lastest model',price='700')
        Product.objects.create(name='Headphones',description='noise cancellation',price='150')
        products = Product.objects.all()
        return render(request, 'products.html', {'products': products})