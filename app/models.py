from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    status = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name
