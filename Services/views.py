from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
import requests
from django.http import HttpResponse
from .serializers import *
import datetime
# Create your views here.

class OrderItemAPIView(APIView):
    def get(self, request, orderItemId):
        order = OrderItem.objects.filter(orderid=orderItemId)
        if order:
            serializer = OrderItemSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        carrier = Carrier.objects.get(id=request.data["carrier"])
        order = OrderItem.objects.create(orderid=request.data["orderid"],
        carrier=carrier,
        shop_id=request.data["shop_id"],
        sender=request.data["sender"],
        reciever=request.data["reciever"],
        sender_location=request.data["sender_location"],
        reciever_location=request.data["reciever_location"])
        if order:
            serializer = OrderItemSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, orderItemId):
        order = OrderItem.objects.get(orderid=orderItemId)
        if order:
            carrier = Carrier.objects.get(id=request.data["carrier"])
            order.carrier=carrier
            order.shop_id=request.data["shop_id"]
            order.sender=request.data["sender"]
            order.reciever=request.data["reciever"]
            order.sender_location=request.data["sender_location"]
            order.reciever_location=request.data["reciever_location"]
            order.save()
            serializer = OrderItemSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class OrderItemShopAPIView(APIView):
    def get(self, request, shopId):
        order = OrderItem.objects.filter(shop_id=shopId)
        if order:
            serializer = OrderItemSerializer(order, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class OrderItemsAPIView(APIView):
    def get(self, request):
        order = OrderItem.objects.all()
        if order:
            serializer = OrderItemSerializer(order, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CarrierAPIView(APIView):
    def get(self, request):
        carriers = Carrier.objects.all()
        product = request.GET.get('productId', '')
        weight = request.GET.get('weight', '')
        if carriers:
            if product:
                response = requests.get('http://stock.phwt.me/product/'+product)
                for carry in carriers:
                    carry.price = carry.price*response.json()["weight"]/1000
            elif weight:
                for carry in carriers:
                    carry.price = carry.price*weight/1000
            for carry in carriers:
                now = datetime.datetime.now() + datetime.timedelta(days=3)
                carry.estimated = now
            serializer = CarrierSerializer(carriers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class OrderDescriptionAPIView(APIView):
    def get(self, request, shippingId):
        order = OrderItem.objects.get(shippingid=shippingId)
        if order:
            description = OrderDescription.objects.filter(orderItem=order)
            serializer = OrderDescriptionSerializer(description, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)