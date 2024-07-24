from rest_framework import serializers
from .models import Menu, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'menu', 'product', 'description', 'price', 'available', 'title', 'image']

class MenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'name', 'description', 'items', 'image_url', 'total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        menu = Menu.objects.create(**validated_data)
        for item_data in items_data:
            MenuItem.objects.create(menu=menu, **item_data)
        return menu
