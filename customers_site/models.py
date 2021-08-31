from django.db import models
from django.contrib.auth.models import User
from survey_app.models import Category, Product, t_date
from django.contrib.auth.middleware import get_user
from . import constants 
# Create your models here.

class ItemModel(models.Manager):
    def get_by_natural_key(self,name):
        return self.get(name=name)

class Preference(models.Model):
    """Preferences of a customer """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product_name = models.CharField(null=True,max_length=250, unique=True)
    product_price = models.DecimalField(null= True,max_digits = 8, decimal_places=2)
    product_category = models.PositiveIntegerField(null=True, choices=constants.CATEGORY_CHOICES)
    like = models.PositiveIntegerField(default = 0)
    created_at =  models.BigIntegerField(default = t_date)
    updated_at = models.BigIntegerField(default = t_date)
    class Meta:
        verbose_name = 'preference'
        verbose_name_plural = "preferences"


class Cart(models.Model):
    """Each user has his own cart"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created_at =  models.BigIntegerField(default = t_date)


class Item(models.Model):
    """This is for each item in the cart"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    objects = ItemModel()
    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def natural_key(self):
        return (self.name, self.id)
        
    def price_ttc(self):
        return self.price_ht * (1 +  constants.TAX_AMOUNT/100.0)

    def __str__(self):
        return  self.client + " - " + self.product
    





