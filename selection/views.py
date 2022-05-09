import json

from django.http import JsonResponse
from rest_framework import request
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from selection.models import Selection
from selection.permissions import IsOwnerAccess
from selection.serializers import SelectionViewSerializer, SelectionCreateSerializer


class SelectionListView(ModelViewSet):
    queryset = Selection.objects.all()
    serializer_class = SelectionViewSerializer

    def get_permissions(self):
        permissions = []
        try:
            if self.action == "retrieve":
                print(IsAuthenticated, 1)
                permissions = (IsAuthenticated,)
            elif self.action in ("update", "partial_update", "destroy", "create"):
                permissions = (IsAuthenticated & (IsAdminUser | IsOwnerAccess),)
                # permissions = (IsOwnerAccess,)
            return [permission() for permission in permissions]
        except KeyError:
            return [permission() for permission in permissions]




    # def create(self, request, *args, **kwargs):
    #     selection_data = SelectionCreateSerializer(data=json.loads(request.body))
    #     if selection_data.is_valid():
    #         selection_data.save()
    #     else:
    #         return JsonResponse(selection_data.errors)
    #     return JsonResponse(selection_data.errors)

    # def get_permissions(self):
    #     try:
    #         permissions = []
    #         if self.action == ("retrieve", 'create'):
    #             permissions = (IsAuthenticated,)
    #         elif self.action in ("update", "partial_update", "destroy"):
    #             permissions = (IsAuthenticated & IsAdminUser,)
    #         return [permission() for permission in permissions]
    #
    #     except KeyError:
    #         return [permission for permission in self.permission_classes]
    #
    #

