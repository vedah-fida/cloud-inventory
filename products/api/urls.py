from django.conf.urls import url
from django.contrib import admin

from .views import ProductListAPIView, ProductDetailAPIView, ProductUpdateAPIView, ProductsCreateUpdateAPIView

urlpatterns = [
    url(r'^$', ProductListAPIView.as_view(), name='products-list'),
    url(r'^create$', ProductsCreateUpdateAPIView.as_view(), name='products-update'),
    url(r'^(?P<product_barcode>\d+)/$', ProductDetailAPIView.as_view(), name='products-details'),
    url(r'^(?P<product_barcode>\d+)/update/$', ProductUpdateAPIView.as_view(), name='products-details-update'),

]
