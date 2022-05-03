from django.contrib.auth.models import User
from rest_framework import serializers

from user_continued.models import LocationUser, ContinuedUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUser
        fields = '__all__'


class ContinuedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinuedUser
        fields = '__all__'


