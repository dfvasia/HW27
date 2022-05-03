from rest_framework import serializers

from ads.models import Advertisement, Characteristics


class AdvViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'


class CatViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = '__all__'
