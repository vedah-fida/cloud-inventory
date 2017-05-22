from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from .models import Products, Category, Items
import datetime

today = datetime.datetime.now()


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
    return render(request, 'product/index.html', {"products_data": products_data})


def in_stock(request):
    products_in_stock = Products.objects.filter(product_stock=True)
    return render(request, 'product/in-stock.html', {"products_in_stock": products_in_stock})


def out_of_stock(request):
    products_out_of_stock = Products.objects.filter(product_stock=False)
    return render(request, 'product/out-of-stock.html', {"products_out_of_stock": products_out_of_stock})


# get products added today
def added_today(request):
    product_added_today = Products.objects.filter(product_date=datetime.datetime.now())
    return render(request, 'product/products_added_today.html', {'product_added_today': product_added_today})


# get products added today
def added_yesterday(request):
    product_added_yesterday = Products.objects.filter(product_date=datetime.datetime.now() - datetime.timedelta(days=1))
    return render(request, 'product/products_added_yesterday.html',
                  {'product_added_yesterday': product_added_yesterday})


# get products added week


# get products added this month
def added_this_month(request):
    #today = datetime.datetime.now()
    products_added_this_month = Products.objects.filter(product_date__month=today.month)
    return render(request, 'product/products_added_this_month.html',
                  {'products_added_this_month': products_added_this_month})

"""
# search barcode entered by user
def barcode_search(request):
    if request.method == 'POST':
        search_barcode = request.POST.get('barcode_search', None)
        try:
            barcode = Products.objects.get(product_barcode=search_barcode)
            return HttpResponse(barcode)
        except Products.DoesNotExist:
            return HttpResponse("Product not found")
    else:
        return render(request, 'product/barcode_search.html')
"""