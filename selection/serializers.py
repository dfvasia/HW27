from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers

from ads.models import Advertisement
from selection.models import Selection


class SelectionViewADSSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Advertisement
        fields = ['id', 'name', "price", "description", "is_published", "image", "author", "category"]


class SelectionViewSerializer(serializers.ModelSerializer):
    ad = SelectionViewADSSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Selection
        fields = ['id', 'name', 'create_at', 'owner', 'ad']


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    ad = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Advertisement.objects.all(),
        slug_field="pk"
    )

    class Meta:
        model = Selection
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._ads = self.initial_data.pop("ads", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        selection = Selection.objects.create(**validated_data)

        for ad in self._ads:
            ad_obj, _ = Selection.objects.get_or_create(name=ad)
            Selection.ad.add(ad_obj)

        Selection.save()

        return selection
