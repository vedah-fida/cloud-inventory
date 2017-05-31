from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Products, Category, Items
import datetime
from products.serializers import ProductsSerializer
from rest_framework import generics

today = datetime.datetime.now()


# Create your views here.
@login_required(login_url='/')
def products_base(request):
    return render(request, 'product/base.html', {})


@login_required(login_url='/')
def products_inner_view(request):
    return render(request, 'product/index.html', {})


@login_required(login_url='/')
# connecting to the database and get the ALL the categories
def get_category(request):
    data = Category.objects.all()
    return render(request, 'product/products_form.html', {"data": data})


@login_required(login_url='/')
# connecting to the database and get the ALL the products
def get_products(request):
    products_data = Products.objects.all()
    return render(request, 'product/index.html', {"products_data": products_data})


@login_required(login_url='/')
def in_stock(request):
    products_in_stock = Products.objects.filter(product_stock=True)
    return render(request, 'product/in-stock.html', {"products_in_stock": products_in_stock})


@login_required(login_url='/')
def out_of_stock(request):
    products_out_of_stock = Products.objects.filter(product_stock=False)
    return render(request, 'product/out-of-stock.html', {"products_out_of_stock": products_out_of_stock})


@login_required(login_url='/')
# get products added today
def added_today(request):
    product_added_today = Products.objects.filter(product_date=datetime.datetime.now())
    return render(request, 'product/products_added_today.html', {'product_added_today': product_added_today})


@login_required(login_url='/')
# get products added today
def added_yesterday(request):
    product_added_yesterday = Products.objects.filter(product_date=datetime.datetime.now() - datetime.timedelta(days=1))
    return render(request, 'product/products_added_yesterday.html',
                  {'product_added_yesterday': product_added_yesterday})


# added this week
def added_this_week(request):
    added_last_week = datetime.datetime.now() - datetime.timedelta(days=7)
    products_added_this_week = Products.objects.filter(product_date__gte=added_last_week)
    return render(request, 'product/products_added_this_week.html',
                  {'products_added_this_week': products_added_this_week})


@login_required(login_url='/')
# get products added this month
def added_this_month(request):
    # today = datetime.datetime.now()
    products_added_this_month = Products.objects.filter(product_date__month=today.month)
    return render(request, 'product/products_added_this_month.html',
                  {'products_added_this_month': products_added_this_month})


@login_required(login_url='/')
# updating the stock status
def update_stock_status(request, products_id):
    Products.objects.filter(pk=products_id).update(product_stock=False)
    products_in_stock = Products.objects.filter(product_stock=True)
    return render(request, 'product/in-stock.html', {"products_in_stock": products_in_stock})


@login_required(login_url='/')
def search_barcode(request):
    search = Products.objects.filter(product_barcode__contains=request.POST['barcode_search'])
    return render(request, 'product/barcode_search.html', {"search": search})


# rest_framework view, it will be a class based view

class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    """
    receive the request, update the database product_stock
    counter check the barcode, update the dbase with the barcode
    return a success or fail message
    """
