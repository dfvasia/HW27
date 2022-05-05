from django.contrib.auth.models import User
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


class ContinuedSerializer(serializers.ModelSerializer):
    local_name = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'


