from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import time
from django.db.models import fields
# Create your models here.
t_date = int(time.mktime(datetime.utcnow().timetuple())*1000)

class CategoryModel(models.Manager):
    def get_by_natural_key(self,name):
        return self.get(name=name)


class Category(models.Model):
    name = models.CharField(null=False,max_length=250, unique=True)
    created_at =  models.BigIntegerField(default = t_date)
    updated_at = models.BigIntegerField(default = t_date)
    objects = CategoryModel()
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name
    
    def natural_key(self):
        return (self.name, self.id)
    
    
    

class Product(models.Model):
    name = models.CharField(null=False,max_length=250, unique=True)
    price = models.DecimalField(max_digits = 8, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at =  models.BigIntegerField(default = t_date)
    updated_at = models.BigIntegerField(default = t_date)

    def __str__(self):
        return self.name


class Log(models.Model):
    transaction_name = models.CharField(null=False,max_length=255)
    transaction_details = models.CharField(null=False, max_length=700)
    created_at =  models.BigIntegerField(default = t_date)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.transaction_name

    