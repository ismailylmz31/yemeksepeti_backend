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
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def update_total_price(self):
        total = sum(item.get_total_price() for item in self.items.all())
        self.total_price = total
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product,blank=True,null=True, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, blank=True,null=True,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        if self.product:
            self.price = self.product.price
        super().save(*args, **kwargs)
       
    def get_total_price(self):
        if self.product and self.price:
            return self.quantity * self.price
        return 0

    def __str__(self):
        return f'{self.product} - {self.quantity}'
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.order.update_total_price()
    
    # def __str__(self):
    #     return f'{self.product.name} ({self.quantity})'
