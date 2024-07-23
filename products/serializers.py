from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Category
        fields = ['id', 'name', 'image_url']

   

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'restaurant', 'category', 'name', 'description', 'price', 'image_url']

   
