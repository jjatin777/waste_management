from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin 

from django.contrib.auth import get_user_model

# Register your models here.
User= get_user_model()

admin.site.register(User)
admin.site.register(address)
admin.site.register(product)