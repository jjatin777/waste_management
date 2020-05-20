from w.models import*
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
import json
import requests
from django.forms.models import model_to_dict



class UserSerializer(serializers.ModelSerializer):
	
	products = serializers.SerializerMethodField('getProductList')
	addresses = serializers.SerializerMethodField('addressList')
	
	print("serializers1")
	def addressList(self,obj):
		try:
			List = address.objects.all().filter(user__id= obj.id)
			print(List)
			
			returnList = []
			for obj in List:
				addr = model_to_dict(obj)
				addr['addrline1'] = obj.addrline1
				addr['addrline2'] = obj.addrline2
				addr['pincode'] = obj.pincode
				addr['city'] = obj.city
				
				returnList.append(addr)
			return returnList
			
		except Exception as e:
			print(e)
			return "error"

	def getProductList(self,obj):
		try:
			productList = product.objects.all().filter(user__username= obj.username)
			productList = productList
			returnList = []
			for obj in productList:
				product1 = model_to_dict(obj)
				product1['category'] = obj.category
				product1['name'] = obj.name
				product1['price'] = obj.price
				product1['description'] = obj.description
				product1['product_image'] = obj.product_image
				returnList.append(product1)
			return returnList
			
		except Exception as e:
			print(e)
			return "error"


	class Meta:

		model = user
		
		fields=['id','contact','password','seller','image','is_superuser','email','username','products','addresses']

		extra_kwargs = {
            'password':{
                'style':{
                    'input_type':'password'
                }
            }
        }

	def create(self, validated_data):

		u = user.objects.create(
			contact=validated_data['contact'],
			seller=validated_data['seller'],
			#image=validated_data['image'],
			is_superuser=validated_data['is_superuser'],
		    email=validated_data['email'],
		    username=validated_data['username']  
		)
		u.set_password(validated_data['password'])
		u.save()
		print("/nin serializer function/n")
		return u



class AddressSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.contact',read_only=True)

	class Meta:
		model = address
		fields = ['id', 'user','addrline1','addrline2','pincode','city']
        

class ProductSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.contact',read_only=True)

	class Meta:
		model = product
		fields = ['id', 'user','category','name','price','description','product_image']
       