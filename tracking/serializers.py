from rest_framework import serializers
from .models import OrderStatus

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['id', 'order', 'status', 'updated_at']
        read_only_fields = ['updated_at']
