from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from .models import Products, Category, Items


# Create your views here.
@login_required
def products_base(request):
    return render(request, 'product/base.html', {})


@login_required
def products_inner_view(request):
    return render(request, 'product/index.html', {})


# connecting to the database and get the ALL the categories
def get_category(request):
    data = Category.objects.all()
    return render(request, 'product/products_form.html', {"data": data})


# connecting to the database and get the ALL the products
def get_products(request):
    products_data = Products.objects.all()
    return render(request, 'product/index.html', {"product_data": products_data})


def in_stock(request):
    products_in_stock = Products.objects.filter(product_stock=True)
    return render(request, 'product/in-stock.html', {'products_in_stock': products_in_stock})


def out_of_stock(request):
    products_out_of_stock = Products.objects.filter(product_stock=False)
    return render(request, 'product/out-of-stock.html', {"products_out_of_stock": products_out_of_stock})
