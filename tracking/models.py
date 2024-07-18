from django.db import models
from orders.models import Order

class OrderStatus(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('On the Way', 'On the Way'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order_statuses')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.order.id} - {self.status}'
