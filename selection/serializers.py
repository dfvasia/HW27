from rest_framework import serializers

from ads.models import Advertisement
from selection.models import Selection


class SelectionViewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Selection
        fields = '__all__'


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
