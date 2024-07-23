from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Profile
        fields = ['id', 'user', 'address', 'phone_number', 'date_of_birth', 'avatar']
        read_only_fields = ['user']

    # def get_avatar_url(self, obj):
    #     request = self.context.get('request')
    #     if obj.avatar:
    #         return request.build_absolute_uri(obj.avatar.url)
    #     return None
