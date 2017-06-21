from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=25)
    category_date = models.DateField()

    def __str__(self):
        return (self.category_name)


class Products(models.Model):
    product_name = models.CharField(max_length=25)
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.IntegerField()
    product_barcode = models.IntegerField()
    product_stock = models.BooleanField(default=True)
    product_date = models.DateField()
    product_count = models.IntegerField(default=0)

    def __str__(self):
        return (self.product_name)


class Items(models.Model):
    COLLECTED = "COLLECTED"
    PROCESSING = "PROCESSING"
    STATUS_CHOICES = (
        (COLLECTED, 'Collected'),
        (PROCESSING, 'Processing'),
    )
    product_code = models.IntegerField()
    product_date = models.DateField()
    product_price = models.IntegerField()
    product_status = models.BooleanField(default=True)

    """
    0 is money collected, 1 is still processing
    """
