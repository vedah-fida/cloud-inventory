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
            'product_name', 'category_type', 'product_price', 'product_barcode', 'product_stock', 'product_date',
            'product_count',

        )


class ProductCheckoutSerializers(ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'product_name', 'product_barcode', 'product_stock', 'product_price', 'product_count',

        )
