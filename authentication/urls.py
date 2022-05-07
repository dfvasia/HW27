from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import *

from authentication.views import UserViewSet, UserAdsView

router = routers.SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('<int:pk>/z/', UserAdsView.as_view()),
]