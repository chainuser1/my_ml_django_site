from django.db import models
from django.contrib.auth.models import User
from survey_app.models import Category, Product, t_date
from . import constants 
# Create your models here.

class Preference(models.Model):
    like_dislike = models.PositiveIntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.OneToOneField(
        Product,
        on_delete = models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name = 'preference'
        verbose_name_plural = "preferences"


class Cart(models.Model):
    """Each user has his own cart"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at =  models.BigIntegerField(default = t_date)


class CartItem(models.Model):
    """This is for each item in the cart"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_ht = models.FloatField(blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)


    def price_ttc(self):
        return self.price_ht * (1 +  constants.TAX_AMOUNT/100.0)

    def __str__(self):
        return  self.client + " - " + self.product
    





