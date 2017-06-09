from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Products, Category, Items
import datetime
from django.core import urlresolvers
from django.shortcuts import HttpResponseRedirect
from django.db.models import Case, Value, When

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
    Products.objects.filter(pk=products_id).update(product_stock=Case
        (
        When(product_stock=True, then=Value(False)),
        default=Value(True)
    ))

    url = urlresolvers.reverse('products:product_details')
    return HttpResponseRedirect(url)


@login_required(login_url='/')
def search_barcode(request):
    search = Products.objects.filter(product_barcode__contains=request.GET['barcode_search'])
    return render(request, 'product/barcode_search.html', {"search": search})


def current_month(request):
    product_month_query = Products.objects.filter(product_date__month=today.month - 1)
    return render(request, 'product/current_month.html', {'product_month_query': product_month_query})


def previous_month(request):
    product_month_query = Products.objects.filter(product_date__month=today.month - 1)
    return render(request, 'product/monthly_report.html', {'product_month_query': product_month_query})


def Reports(request):
    current_month_query = Products.objects.filter(product_date__month=today.month)
    previous_month_query = Products.objects.filter(product_date__month=today.month - 1)
    return render(request, 'product/monthly_report.html',
                  {'current_month_query': current_month_query, 'previous_month_query': previous_month_query})
