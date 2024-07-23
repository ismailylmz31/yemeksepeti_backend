from django.db import models
from products.models import Product
from restaurants.models import Restaurant

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='menu_items')    
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.product.name
