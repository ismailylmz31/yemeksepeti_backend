from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('customer', 'restaurant', 'status', 'created_at', 'total_price')
    search_fields = ('customer__username', 'restaurant__name', 'status')
    list_filter = ('status', 'created_at')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'menu', 'quantity', 'total_price')
    search_fields = ('order__customer__username', 'product__name')
    list_filter = ('order__created_at',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
