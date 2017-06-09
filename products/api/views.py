from rest_framework.generics import (
    ListAPIView, RetrieveAPIView , UpdateAPIView, CreateAPIView
                )
from .serializers import ProductsListSerializers, ProductsDetailSerializers, ProductsCreateUpdateSerializers
from products.models import Products


class ProductListAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializers


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializers
    lookup_field = 'product_barcode'


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializers

class ProductsCreateUpdateAPIView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsCreateUpdateSerializers
