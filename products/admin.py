from django.contrib import admin
from .models import *

# Register your models here.



class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_barcode', 'product_stock', 'product_price', 'product_count',)
admin.site.register(Products, ProductsAdmin)

admin.site.register(Items)

admin.site.register(Category)
