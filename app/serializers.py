from rest_framework import serializers
from .models import *

# class Productserializers(serializers.Serializer):
#     product_name = models.CharField(max_length=100)  # @@@@@ isse to data hi ud gaya
#     price = models.PositiveIntegerField()
#     status = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
# 
#     def __str__(self):
#         return self.product_name



class Productserializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

        