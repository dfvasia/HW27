import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Advertisement, Characteristics


@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request):
        return JsonResponse(
            {
                "status": "ok"
            }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads = Advertisement.objects.all()

        response = []
        for ad in ads:
            response.append(
                {
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author,
                    "description": ad.description,
                    "address": ad.address,
                    "is_published": ad.is_published,
                }
            )
        return JsonResponse(response, status=200, safe=False)


class AdsDetailView(DetailView):
    model = Advertisement

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse(ad(
            {
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
            }
        ), status=200, safe=False)

class CatView(View):
    def get(self, request):
        cats = Characteristics.objects.all()

        response = []
        for cat in cats:
            response.append(
                {
                    "id": cat.id,
                    "name": cat.name,
                }
            )
        return JsonResponse(response, status=200, safe=False)
