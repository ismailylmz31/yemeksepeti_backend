from django.db import models
from users.models import User

class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants_owner')
    name = models.CharField(max_length=255)    
    image_url = models.URLField(null=True,blank=True)    
    address = models.TextField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(null=True,blank=True,default=5)
    min_basket_price = models.DecimalField(default=0,null=True,blank=True,max_digits=3,decimal_places=0)
    delivery_price=models.DecimalField(default=0,null=True,blank=True,max_digits=2,decimal_places=0)
    delivery_time=models.CharField(default='30-45 dk',max_length=400)

    def __str__(self):
        return self.name


class Offer(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurants')
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    is_exist = models.BooleanField(default=False)
    image_url = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title




