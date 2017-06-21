from django.conf.urls import url
from django.contrib import admin

from .views import ProductListAPIView, ProductDetailAPIView, ProductUpdateAPIView, ProductsCreateUpdateAPIView, \
    CheckOutProduct

urlpatterns = [
    url(r'^$', ProductListAPIView.as_view(), name='products-list'),
    url(r'^(?P<product_barcode>\d+)/$', ProductDetailAPIView.as_view(), name='products-details'),
    url(r'^(?P<product_barcode>\d+)/update/$', ProductUpdateAPIView.as_view(), name='products-details-update'),
    url(r'^(?P<product_barcode>\d+)/create/$', ProductsCreateUpdateAPIView.as_view(), name='products-details-update'),
    url(r'^product/checkout/(?P<product_barcode>[0-9]+)/$', CheckOutProduct.as_view(),
        name='products-checkout'),

]
