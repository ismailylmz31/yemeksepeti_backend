from rest_framework import serializers

from products.serializers import CategorySerializer
from .models import Offer, Restaurant

class RestaurantSerializer(serializers.ModelSerializer):    
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = ['id', 'owner', 'name', 'address', 'phone', 'created_at', 'updated_at','image_url','rating','categories','min_price']
        read_only_fields = ['owner']

    # def get_image_url(self, obj):
    #     request = self.context.get('request')
    #     if obj.image:
    #         return request.build_absolute_uri(obj.image.url)
    #     return None

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user
        return super().create(validated_data)

class OfferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Offer
        fields = ['title','description','is_exist','image_url','restaurants']
    



