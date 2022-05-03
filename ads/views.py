import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet

from HW27 import settings
from ads.models import Advertisement, Characteristics
from ads.serializer import AdvViewSerializer, CatViewSerializer


@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request):
        return JsonResponse(
            {
                "status": "ok"
            }, status=200)


class AdvViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvViewSerializer

    def list(self, request, *args, **kwargs):
        adv_data = request.GET.get('cat', None)

        if adv_data:
            self.queryset = self.queryset.filter(
                category__in=adv_data
            )
        return super().list(request, *args, **kwargs)


class CatViewSet(ModelViewSet):
    queryset = Characteristics.objects.all()
    serializer_class = CatViewSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdsImageUpdateView(UpdateView):
    model = Advertisement
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES("image")
        self.object.save()

        return JsonResponse({
            "id":  self.object.id,
            "name":  self.object.name,
            "author_id":  self.object.author_id,
            "author":  list(map(str, self.object.author.all())),
            "price":  self.object.price,
            "description":  self.object.description,
            "is_published":  self.object.is_published,
            "category_id":  self.object.category,
            "image": self.object.image.url if self.object.image else None,
        }, status=200, safe=False)
