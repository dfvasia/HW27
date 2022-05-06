from django.urls import path, include
from rest_framework import routers

from authentication.views import UserViewSet, UserAdsView

router = routers.SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/z/', UserAdsView.as_view()),
]