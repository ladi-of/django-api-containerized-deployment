from rest_framework import serializers
from .models import UserSpec


class UserSpecSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')

    class Meta:
        model = UserSpec
        fields = ['id', 'name']
