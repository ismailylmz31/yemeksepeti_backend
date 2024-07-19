from django.contrib import admin
from .models import  OrderStatus




class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'updated_at')
    search_fields = ('order__customer__username', 'order__restaurant__name', 'status')
    list_filter = ('updated_at',)


admin.site.register(OrderStatus, OrderStatusAdmin)