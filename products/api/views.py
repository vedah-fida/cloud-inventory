from django.db.models import Q
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
)
from .serializers import ProductsListSerializers, ProductsDetailSerializers, ProductsCreateUpdateSerializers
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


class ProductCreateUpdateApiView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsCreateUpdateSerializers
    permission_classes = [IsAdminUser, IsOwnerOrReadOnly]


class ProductListAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializers
    filter_backends = [SearchFilter]
    search_fields = ['product_barcode']


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
    filter_backends = [SearchFilter]
    search_fields = ['product_barcode']
