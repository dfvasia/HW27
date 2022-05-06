from django.urls import path, include
from rest_framework import routers

from ads.views import AdvViewSet, AdsImageUpdateView

router = routers.SimpleRouter()
router.register('', AdvViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/upload_image/', AdsImageUpdateView.as_view()),
    ]


