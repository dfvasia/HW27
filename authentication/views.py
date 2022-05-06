from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Count, Avg
from django.http import JsonResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet

from HW27 import settings
from authentication.models import LocationUser, User
from authentication.serializer import UserSerializer, LocationSerializer, ContinuedSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(ModelViewSet):
    queryset = LocationUser.objects.all()
    serializer_class = LocationSerializer


class ContinuedViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ContinuedSerializer


class UserAdsView(View):
    def get(self, request, *args, **kwargs):
        user_qs = User.objects.all().annotate(ads=Count('advertisement')).filter(advertisement__is_published__exact=True)

        paginator = Paginator(user_qs, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        users = []

        for user in page_obj:
            users.append(
                {
                    "id": user.id,
                    "name": user.username,
                    "total_ads": user.ads,
                }
            )

        response = {
            "items": users,
            "num_pages": paginator.num_pages,
            "total": paginator.count,
            "avg": user_qs.aggregate(avg=Avg("ads"))["avg"],
        }

        return JsonResponse(response, safe=False)
