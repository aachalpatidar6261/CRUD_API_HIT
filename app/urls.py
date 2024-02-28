from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('product_crud',views.Product_crud.as_view(),name='product_crud'),

    path('product_crud/<int:pk>',views.Product_crud.as_view(),name='product_crud'),
    path('register_user/',views.register_user, name='register'),
    
]

