from rest_framework import serializers

from authentication.models import LocationUser, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUser
        fields = '__all__'
