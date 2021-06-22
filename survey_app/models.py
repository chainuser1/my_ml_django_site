from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.db.models import fields
# Create your models here.

class Category(models.Model):
    name = models.CharField(null=False,max_length=250, unique=True)
    created_at =  models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(null=False,max_length=250, unique=True)
    price = models.DecimalField(max_digits = 8, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at =  models.DateTimeField(default = datetime.now())
    updated_at = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return self.name


class Log(models.Model):
    transaction_name = models.CharField(null=False,max_length=255)
    transaction_details = models.CharField(null=False, max_length=700)
    created_at =  models.DateTimeField(default = datetime.now())
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.transaction_name
    
    @property
    def get_user(self):
        return '%s' % self.user.username
    