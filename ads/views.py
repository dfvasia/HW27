from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.models import Advertisement, Characteristics
from ads.serializer import AdvViewSerializer, CatViewSerializer
from authentication.models import LocationUser


@method_decorator(csrf_exempt, name='dispatch')
class MainView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "status": "ok"
            }, status=200)


class AdvViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvViewSerializer

    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [AllowAny],
                                    'retrieve': [IsAuthenticated],
                                    'update': [IsAuthenticated],
                                    'perform_update': [IsAuthenticated],
                                    'destroy': [IsAuthenticated],
                                    }

    def list(self, request, *args, **kwargs):

        adv_cat = request.GET.get('cat', None)
        adv_text = request.GET.get('text', None)
        adv_local = request.GET.get('location', None)
        adv_price_to = request.GET.get('price_to', None)
        adv_price_from = request.GET.get('price_from', None)

        if adv_cat:
            self.queryset = self.queryset.filter(
                category__in=adv_cat
            )
        if adv_text:
            self.queryset = self.queryset.filter(
                description__icontains=adv_text
            )
        if adv_local:
            self.queryset = self.queryset.filter(
                author__continueduser__location__in=[i.id for i in LocationUser.objects.all().filter(name__icontains=adv_local)]
            )
        if adv_price_to and adv_price_from:
            self.queryset = self.queryset.filter(
                price__lte=adv_price_to,
                price__gte=adv_price_from
            )
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CatViewSet(ModelViewSet):
    queryset = Characteristics.objects.all()
    serializer_class = CatViewSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdsImageUpdateView(UpdateView):
    model = Advertisement
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id":  self.object.id,
            "name":  self.object.name,
            "author_id":  self.object.author_id,
            "author":  self.object.author.username,
            "price":  self.object.price,
            "description":  self.object.description,
            "is_published":  self.object.is_published,
            "category_id":  self.object.category_id,
            "category":  self.object.category.name,
            "image": self.object.image.url if self.object.image else None,
        }, status=200, safe=False)
