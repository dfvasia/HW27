from django.urls import path, include
from rest_framework import routers

from selection.views import SelectionListView

router = routers.DefaultRouter()
router.register('', SelectionListView)


urlpatterns = [
    # path('', SelectionListView.as_view()),
    path('', include(router.urls)),
    ]
