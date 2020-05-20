from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


categ= [('Electronics and appliances','Electronics and appliances'),('Hair','Hair'),('Clothing','Clothing'),('Stationary','Stationary')]


class UserManager(BaseUserManager):


	def create_user(self, email,username,contact,password,seller= False,is_staff=False,is_superuser=False):
		
		print("create_user")
		if not email:
		    raise ValueError('Users must have an email address')
		if not username:
			raise ValueError("uername not provided")
		if not contact:
			raise ValueError('contact not provided')

		email = self.normalize_email(email)

		user = self.model(
			email=email,
			username = username,
			seller = seller,
			contact = contact)
		user.is_staff = is_staff
		user.is_superuser= is_superuser
		user.is_active = True
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_staffuser(self,email,username,contact,password,seller= False):
		
		user = self.create_user(
			email,
			username,
			contact,
			password,
			seller,
			is_staff=True
		)

		return user

	def create_superuser(self,email,username,contact,password,seller= False):
		
		user = self.create_user(
			email,
			username,
			contact,
			password,
			seller,
			is_superuser= True,
			is_staff=True
		)
		
		return user


class user(AbstractBaseUser,PermissionsMixin):
	
	image  = models.ImageField(default= 'default.jpg',upload_to = 'media')
	email = models.EmailField(verbose_name='email address',unique=True,max_length=255,null = True)
	username= models.CharField(max_length= 200,default='username')
	seller = models.BooleanField(default=False)
	contact= models.CharField(max_length= 10,unique=True,default=123456789)
	is_active = models.BooleanField(default=True)
	is_superuser=models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)



	objects = UserManager()

	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['username','contact']

	def __str__(self):
		return self.contact

	
	@property
	def first_name(self):
		return self.username

	@property
	def last_name(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser


		
class address(models.Model):
	user = models.ForeignKey(user,on_delete = models.CASCADE,null = False)
	addrline1= models.CharField(max_length= 500,null = False)
	addrline2= models.CharField(max_length= 500,null = False)
	pincode= models.IntegerField()
	city= models.CharField(max_length=200)



class product(models.Model):
	product_image = models.ImageField(null = 'True',upload_to = 'media')
	user = models.ForeignKey(user,on_delete = models.CASCADE,null = False)
	category = models.CharField(choices = categ, null = False,max_length=100)
	name = models.CharField(max_length=500)
	price = models.IntegerField()
	description = models.CharField(max_length=500)


