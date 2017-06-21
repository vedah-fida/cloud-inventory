from django.db.models import Q
from rest_framework import generics
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView, UpdateAPIView
)
from .serializers import ProductsListSerializers, ProductsDetailSerializers, ProductsCreateUpdateSerializers, \
    ProductCheckoutSerializers
from products.models import Products

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly

from  rest_framework.filters import (
    SearchFilter, OrderingFilter,
)
from .pagination import ProductLimitOffsetPagination


class ProductCreateUpdateApiView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsCreateUpdateSerializers
    permission_classes = [IsAdminUser, IsOwnerOrReadOnly]


class ProductListAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializers
    filter_backends = [SearchFilter]
    search_fields = ['product_barcode']
    pagination_class = ProductLimitOffsetPagination


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializers
    lookup_field = 'product_barcode'


class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializers
    lookup_field = 'product_barcode'


class ProductsCreateUpdateAPIView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsCreateUpdateSerializers
    lookup_field = 'product_barcode'


class CheckOutProduct(RetrieveUpdateAPIView):
    serializer_class = ProductCheckoutSerializers

    def get(self, request, product_barcode):
        instance = Products.objects.get(product_barcode=product_barcode)
        if instance.product_count > 0:
            instance.product_stock = True
            new_count = instance.product_count - 1
            if new_count is 0:
                instance.product_stock = False
                instance.product_count = new_count
                instance.save()
                serializer = ProductCheckoutSerializers(instance)
                return Response(serializer.data)

            else:
                instance.product_count = new_count
                instance.save()
                serializer = ProductCheckoutSerializers(instance)
                return Response(serializer.data)
        else:
            msg = {"msg": "Out of Stock"}
            return Response(msg)
