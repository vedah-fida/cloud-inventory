from django.conf.urls import include, url

from . import views

app_name = "products"

urlpatterns = [
    # url(r'^$', views.products_base, name="products"),

    # this view displays the redirected page after login. It also displays all the products(in and out of stock)
    url(r'view', views.get_products, name="product_details"),

    # display IN STOCK products
    url(r'^in-stock/$', views.in_stock, name="in-stock"),

    # display OUT OF STOCK products
    url(r'^out-of-stock/$', views.out_of_stock, name="out-of-stock"),

    # this view is used for testing purposes, its contents may change frequently
    url(r'category/$', views.in_stock, name="get_category"),

]
