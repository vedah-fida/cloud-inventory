from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "products"

urlpatterns = [
    # url(r'^$', views.products_base, name="products"),

    # this view displays the redirected page after login. It also displays all the products(in and out of stock)
    url(r'view/$', views.get_products, name="product_details"),

    # display IN STOCK products
    url(r'^in-stock/$', views.in_stock, name="in-stock"),

    # display OUT OF STOCK products
    url(r'^out-of-stock/$', views.out_of_stock, name="out-of-stock"),

    # search for products added today
    url(r'^today', views.added_today, name="product_added_today"),

    # search for products added yesterday
    url(r'^yesterday', views.added_yesterday, name="products_added_yesterday"),

    # search for products added this week
    url(r'^this-week', views.added_this_week, name="products_added_this_week"),

    # search for products added this month
    url(r'^month', views.added_this_month, name="products_added_this_month"),

    # search for barcode entry by user
    url(r'^search_barcode/$', views.search_barcode, name="search_barcode"),

    # search for barcode entry by user
    url(r'^stock_status/(?P<products_id>[0-9]+)/$', views.update_stock_status, name="stock_status"),

    #monthly_report
    url(r'^current-month-report', views.ReportsView.as_view(), name="products_reports"),


    #url(r'^test', views.previous_month, name="products_reports"),

    # serialized data
    url(r'^products/$', views.ProductsList.as_view(), name='product_list'),

    # serialized data
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductsDetail.as_view(), name='product_detail'),

    # this view is used for testing purposes, its contents may change frequently
    url(r'^category/$', views.in_stock, name="get_category"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
