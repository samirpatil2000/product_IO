from django.contrib import admin

# Register your models here.
from .models import Product,ProductInCart,Order


admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Order)
