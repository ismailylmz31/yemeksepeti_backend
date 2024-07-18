from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'address', 'phone_number', 'date_of_birth']
        read_only_fields = ['user']
