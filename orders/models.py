from django.db import models
from django.contrib.auth import get_user_model
from menus.models import Menu
from products.models import Product
from restaurants.models import Restaurant

User = get_user_model()

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='Pending')
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def price(self):
        if self.product:
            return self.product.price
        elif self.menu:
            return self.menu.price
        return 0

    @property
    def total_price(self):
        return self.price * self.quantity
