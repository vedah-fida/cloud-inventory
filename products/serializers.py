from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_name', 'product_barcode', 'product_stock')


