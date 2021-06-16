from django.db import models

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
    created_at =  models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    

    