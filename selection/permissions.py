from rest_framework import permissions

from selection.models import Selection


class IsOwnerAccess(permissions.BasePermission):
    message = 'Вы не владелец'

    def has_permission(self, request, view):
        if request.user.id == Selection.objects.get(pk=request.path[-2:-1]).owner_id:
            return True
        return False

