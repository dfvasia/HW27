from django.urls import path, include
from rest_framework import routers

from selection.views import SelectionListView

router = routers.SimpleRouter()
router.register('', SelectionListView)


urlpatterns = [
    path('', SelectionListView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', SelectionListView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('', include(router.urls)),
    ]
