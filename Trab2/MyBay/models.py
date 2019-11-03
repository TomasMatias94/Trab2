# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import AbstractUser 
from django_countries.fields import CountryField
from datetime import datetime    
from django.utils.timezone import now

from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.


class CustomUser(AbstractUser): 
    #pass
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address= models.CharField(max_length=100)
    country = CountryField()
    username=models.CharField(max_length=20, unique=True, null=False)
    
    def __str__(self):
        return self.email

from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model): 
    id= models.AutoField(primary_key=True)    
    owner=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0.00)])
    title=models.CharField(max_length=50)
    descr=models.TextField(default="no description", null=False)
    product_image = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(default=now, editable=False)
    country = CountryField()
    category= models.CharField(
        max_length=2,
        choices=[('1', 'Clothes'),('2', 'Comics'), ('3', 'Figures'), ('4', 'Games'), ('5', 'Others')],
        default='5',
    )
    
    def __str__(self):
        return str(self.id)


@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.product_image.delete(False)