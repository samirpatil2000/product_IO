from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    price = models.IntegerField(default=10,validators=[
        MinValueValidator(1)])
    desc = models.TextField(default="This is the desc of product")
    seller = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class ProductInCart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,validators=[
        MinValueValidator(1),MaxValueValidator(10)])

class Order(models.Model):
    products_in_cart=models.ManyToManyField(ProductInCart)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_active= models.BooleanField(default=True)
    is_completed= models.BooleanField(default=False)
    purchase_date=models.DateTimeField(auto_now_add=True)

