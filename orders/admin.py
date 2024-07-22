from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'restaurant', 'status', 'created_at')
    search_fields = ('customer__username', 'restaurant__name', 'status')
    list_filter = ('status', 'created_at')
    inlines = [OrderItemInline]



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__customer__username', 'product__name')
    list_filter = ('order__created_at',)    


admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
