# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Product#, Person

'''
# Register your models here.
class CustomUserAdmin(UserAdmin):
    #add_form=CustomUserCreationForm
    #form=CustomUserChangeForm
    model=CustomUser
    list_display=['email', 'username', 'country']
'''

'''
class ProductAdmin():
    add_form=ProductCreationForm
    form=ProductCreationForm
    model=Product
    list_display=['owner', 'title', 'descr']#, 'product_image']
'''
#admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)
admin.site.register(Product)
#admin.site.register(Person)