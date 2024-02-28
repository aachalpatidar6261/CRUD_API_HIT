import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from.serializers import *
from .models import *

#from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt #it hndle csrf 

def index(request):
    return Response("Index Page")

# 4 method of request = get post put delete.
#@api_view(['GET', 'PUT', 'DELETE','POST'])

#@csrf_exempt
class Product_crud(APIView):
    
    def post(self, request):         
        # body_unicode = request.body.decode('utf-8') # body data come on encode so need to convert in decode
        # data=json.loads(body_unicode)
        # product_name = data["product_name"]
        # price = data["price"]
        # status = data["status"]
        # category = data["category"]
        # product = Product(product_name = product_name, price =price , status = status, category=category)
        # product.save()
        serializers=Productserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response({"Message":"Product added successfully!"},status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if pk == None:
            product = Product.objects.all()
            serializers = Productserializers(product, many=True)
            print(serializers,"12345678")
            return Response(serializers.data)
           
        else:
            product = Product.objects.get(pk=pk)
            serializers = Productserializers(product)
            return Response(serializers.data)
       
        #    product_store =[]              
        #    data = {
        #        'Product_Name' : product.product_name,
        #        'Price' : product.price,
        #        'Status' : product.status,
        #        'Category' : product.category
        #    } 
        #    product_store.append(data)
        #    return Response(product_store)


    def patch(self, request, pk):        
        product = Product.objects.get(pk=pk)
        serializers = Productserializers(product, data=request.data,partial=True)  # partial help to update perticular fields
        
        if serializers.is_valid():
            serializers.save()
            return Response({"data":serializers.data,"Message":"Product Updated successfully!"})
        return Response({"data":serializers.errors,"Message":"Product Updated successfully!"})

        # if product_name:
        #     product.product_name = product_name
        # if price:
        #     product.price = price
        # if status:
        #     product.status = status
        # if category:
        #     product.category = category
        # product.save()
        # return Response({"Message":"Product Updated successfully!"},status=status.HTTP_200)
       
    def delete(self, request, pk):
       product = Product.objects.get(pk=pk)
       product.delete()
       return Response({"Message":"Product Delete successfully!"})

@csrf_exempt    
def register_user(request):    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')   
    
        register_url = "ulr" # write url where to hit api 
        payload = {

            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name
        }
            
        response = requests.post(register_url, data=payload)    
        return HttpResponse(response,{'message':'User registered successfully'})
        # if response.status_code == 201:  # Assuming 201 is the status code for successful registration
        #     return JsonResponse({'message': 'User registered successfully'}, status=201)
        # else:
        #     return JsonResponse({'error': 'Registration failed'}, status=response.status_code)

    return HttpResponse("Method not allowed", status=405)