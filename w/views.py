from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from .models import*
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import*
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.contrib.auth import authenticate




class product_list(APIView):
  
    def get(self, request, format=None):
        products = product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user= self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class product_detail(APIView):


    def get_object(self, pk):
        try:
            return product.objects.get(pk=pk)
        except product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product,context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save(user= self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class address_list(APIView):
      
    def get(self, request, format=None):
        addresss = address.objects.all()
        serializer = AddressSerializer(addresss,many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        address = AddressSerializer(data=request.data)
        if address.is_valid():
            address.save(user=self.request.user)
            return Response(address.data, status=status.HTTP_201_CREATED)
        return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)


class address_detail(APIView):
  

    def get_object(self, pk):
        try:
            return address.objects.get(pk=pk)
        except address.DoesNotExist:
            raise Http404

    def get(self, request,pk,  format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address,context={'request': request})
        return Response(serializer.data)

    def put(self, request,pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save(user= self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class user_list(APIView):
    authentication_classes = []
    permission_classes = []

    queryset = user.objects.all()
    serializer_class = UserSerializer


    def get(self, request, format=None):
        users = user.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    # def post(self, request,format=None):
    #     user = UserSerializer(data=request.data)
    #     data={}
    #     print(user)
    #     print(request.data)
    #     if user.is_valid():
    #         x = user.save()
    #         user = authenticate(username=request.data['username'],password = request.data['password'])
    #         #x=user.save() 
    #         token= Token.objects.get(user=user).key
    #         data['token']=token
    #         return Response(data, status=status.HTTP_201_CREATED)
    #     return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    # self.user = authenticate(**params, password=password)

    def post(self, request,format=None):

        
        user = UserSerializer(data=request.data)
        if user.is_valid():
            x= user.save()
      
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


class user_detail(APIView):

    def get_object(self, contact):
        try:
            return user.objects.get(contact=contact)
        except user.DoesNotExist:
            raise Http404

    def get(self, request, contact, format=None):
        user = self.get_object(contact)
        serializer = UserSerializer(user,context={'request': request})
        return Response(serializer.data)

    def put(self, request, contact, format=None):
        user = self.get_object(contact)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, contact, format=None):
        user = self.get_object(contact)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)