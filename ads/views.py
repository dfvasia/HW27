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

"""
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from DP27.models import Vacancy


@method_decorator(csrf_exempt, name="dispatch")
class VacancyView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()

        search_text = request.GET.get("text", None)
        if search_text:
            vacancies = vacancies.filter(text=search_text)

        response = []
        for vacancy in vacancies:
            response.append({
                "id": vacancy.id,
                "text": vacancy.text,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        vacancy_data = json.loads(request.body)

        vacancy = Vacancy()
        vacancy.text = vacancy_data["text"]

        vacancy.save()
        return JsonResponse({
            "id": vacancy.id,
            "text": vacancy.text
        })


class VacancyDetailView(DetailView):
    model = Vacancy

    def get(self, request, *args, **kwargs):
        vacancy = self.get_object()
        return JsonResponse({
                "id": vacancy.id,
                "text": vacancy.text,
            })
"""