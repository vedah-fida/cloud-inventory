from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=25)
    product_manufacturer = models.CharField(max_length=25)

    def __str__(self):
        return self.product_name + ' - ' + self.product_category + ' - ' + self.product_manufacturer


class Barcode(models.Model):
    product_name = models.ForeignKey(Product, max_length=50)
    category_name = models.CharField(max_length=50)
    barcode = models.IntegerField()

    def __str__(self):
        return str(self.barcode)


class Quantity(models.Model):
    product_name = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name + '-' + self.category_name + '-' + str(self.stock_quantity)
