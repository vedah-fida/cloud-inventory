from rest_framework.serializers import ModelSerializer
from products.models import Products


class ProductsListSerializers(ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'product_name', 'product_barcode', 'product_stock',

        )
class ProductsDetailSerializers(ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'product_name', 'product_barcode', 'product_stock', 'product_price',

        )
class ProductsCreateUpdateSerializers(ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'product_name', 'product_barcode',

        )
"""
data = {
    "product_name" : "Guiness",
    "product_barcode" : "99999999",
    "product_stock" : "True",

}
"""


