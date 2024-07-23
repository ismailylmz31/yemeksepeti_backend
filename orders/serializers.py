from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField(source='get_total_price')
    product_name = serializers.ReadOnlyField(source='menu_item.product.name')
    product_price = serializers.ReadOnlyField(source='menu_item.product.price')

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product_name', 'product_price', 'quantity', 'total_price', 'menu']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'restaurant', 'created_at', 'updated_at', 'status', 'items','total_price']
        read_only_fields = ['customer', 'created_at', 'updated_at','total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        order.update_total_price()  # total price'ı hesapla ve güncelle
        return order
