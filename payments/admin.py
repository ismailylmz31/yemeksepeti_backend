from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_method', 'created_at')
    search_fields = ('order__customer__username', 'order__restaurant__name', 'payment_method')
    list_filter = ('created_at',)

admin.site.register(Payment, PaymentAdmin)