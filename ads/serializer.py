from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ads.models import Advertisement, Characteristics


class NotIsPublishedValidator:
    def __init__(self, is_true):
        self.is_true = is_true

    def __call__(self, value):
        if value == self.is_true:
            raise serializers.ValidationError("нельзя сразу опубликовать")


class AdvViewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
        min_length=10,
        validators=[UniqueValidator(queryset=Advertisement.objects.all())],
        )

    is_published = serializers.BooleanField(validators=[NotIsPublishedValidator(True)])

    class Meta:
        model = Advertisement
        fields = '__all__'


class CatViewSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(
        max_length=10,
        min_length=5,
        validators=[UniqueValidator(queryset=Characteristics.objects.all())],
    )
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Characteristics
        fields = '__all__'
