
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProductSerializer,UserSerializer,OrderSerializer
from django.contrib.auth.models import User
from .models import Product,ProductInCart,Order

from rest_framework.authtoken.models import Token
import requests,json


@api_view(['GET'])

def getProductList(request):
    if request.method == 'GET':
        data = Product.objects.all()
        serializer = ProductSerializer(data,many=True)
        return Response(serializer.data)
    return Response({"message" :"Check Your request method" })

@api_view(['GET'])

def getProduct(request:HttpRequest,pk:int):
    if request.method == 'GET':
        try:
            data = Product.objects.get(id=pk)
        except:
            return HttpResponse(status=404)
        serializer = ProductSerializer(data)
        return Response(serializer.data)
    return Response({"message": "Check Your request method"})


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def createProduct(request: HttpRequest):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response({"message": "Check Your request method"})

@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated,])
def updateProduct(request: HttpRequest,pk:int):
    if request.method == 'PUT':
        try:
            data = Product.objects.get(id=pk)
        except:
            return HttpResponse(status=404)

        serializer = ProductSerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response({"message": "Check Your request method"})

@csrf_exempt
@api_view(['POST'])
def get_or_createUser(request):
    data={}
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        print(request.data)

        if User.objects.filter(username=request.data["username"]).exists():
            user = User.objects.get(username=request.data["username"])
            data["message"]="User has been already created!"
            token = Token.objects.get_or_create(user_id=user.id)[0].key
            data["data"]={
                "username":user.username,
                "token":token,
                "id":user.id,
            }
            return Response(data, status=201)

        if serializer.is_valid():
            account = serializer.save()
            account.save()
            token = Token.objects.get_or_create(user_id=account.id)[0].key
            data['username'] = account.username
            data['token'] = token
            data['id'] = account.id
        else:
            data=serializer.errors

        return Response(data, status=201)

    return Response({"message": "Check Your request method"})

def getSingleOrder(order:'Order')->dict:
    order_data = {}
    order_data["order_id"] = order.id
    order_data["user"] = str(order.user)
    order_data["purchase_date"] = str(order.purchase_date)
    order_data["products_in_cart"] = []

    for prod_in_cart in order.products_in_cart.all():
        prod = Product.objects.get(id=prod_in_cart.product.id)
        prod_data = {}
        prod_data["product_id"] = prod.id
        prod_data["product_name"] = prod.name
        prod_data["product_price"] = prod.price
        prod_data["product_desc"] = prod.desc

        order_data["products_in_cart"].append(
            {'product': prod_data, 'quantity': prod_in_cart.quantity}
        )
    return order_data

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def getUserOrders(request:HttpRequest,username:str):
    if request.method == 'GET':
        try:
            orders = Order.objects.filter(username=username,is_active=True)
            data=[]
            for order in orders:
                data.append(
                    getSingleOrder(order)
                )
            return Response(json.dumps(*data))
        except Exception as e:
            return Response({"status": "404","message": "User Does Not Exist"})

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def getOrders(request:HttpRequest):
    if request.method == 'GET':
        try:
            orders = Order.objects.filter(is_active=True)
            data=[]
            for order in orders:
                data.append(
                    getSingleOrder(order)
                )
            return Response(json.dumps(data))
        except Exception as e:
            return Response({"status": "404","message": "User Does Not Exist"})

