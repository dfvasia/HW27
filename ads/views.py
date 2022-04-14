from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request):
        return JsonResponse(
            {
                "status": "ok"
            }, status=200)


class AdsView(View):
    def get(self, request):
        return JsonResponse(
            {
                "status": "ok"
            }, status=200)


class CatView(View):
    def get(self, request):
        return JsonResponse(
            {
                "status": "ok"
            }, status=200)
