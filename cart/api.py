from .models import Product
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import generics
from django.http import Http404


class UserAPI(APIView):
    def get(self, request):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

    def post(self, request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductAPI(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentAPI(APIView):
    def get(self, request, format=None):
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return Response(serializer.data)

class OrderAPI(APIView):
    def get(self, request, format=None):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


