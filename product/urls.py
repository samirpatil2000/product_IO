from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('getProductList/', getProductList),
    path('getProduct/<int:pk>/',getProduct),
    path('createProduct/',createProduct),
    path('createUser/',get_or_createUser),
    path('updateProduct/<int:pk>/',updateProduct),
    path('getOrders/',getOrders),
    path('getUserOrders/<str:username>',getOrders),


]
urlpatterns = format_suffix_patterns(urlpatterns)