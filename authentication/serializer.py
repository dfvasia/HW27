from rest_framework import serializers
from authentication.models import LocationUser, User


class BanRambler:
    def __call__(self, value):
        domain = value[value.index('@')+1:].lower()
        print(domain)
        if domain == 'rambler.ru':
            raise serializers.ValidationError("Домен запрещен")


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[BanRambler()])

    class Meta:
        model = User
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUser
        fields = '__all__'
